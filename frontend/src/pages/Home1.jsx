import React, { useState, useEffect, useRef } from 'react';
import { Calendar, Mic, Send, ImageIcon, X } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

// Mock store and translation function for demo
const useAppStore = () => ({
  selectedLanguage: 'en'
});

const getTranslation = (lang, key) => {
  const translations = {
    appTitle: 'Project Kisan',
    welcome: 'Welcome to Project Kisan! How can I help you today?',
    enterText: 'Type your question here...',
    ask: 'Ask',
    listening: 'Listening... Speak now'
  };
  return translations[key] || key;
};

const Home = () => {
  const { selectedLanguage } = useAppStore();
  const [inputText, setInputText] = useState('');
  const [isListening, setIsListening] = useState(false);
  const [messages, setMessages] = useState([]);
  const [hasStartedChat, setHasStartedChat] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [selectedImage, setSelectedImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [transcript, setTranscript] = useState('');
  const [micError, setMicError] = useState('');
  const speechRecognitionRef = useRef(null);
  const silenceTimeoutRef = useRef(null);
  const fileInputRef = useRef(null);

  // API Configuration (unchanged)
  const API_BASE_URL = window.location.hostname.includes('cloudworkstations.dev') 
    ? `https://${window.location.hostname.replace('5173-', '8000-')}`
    : 'http://localhost:8000';
  const APP_NAME = 'kisan_agent';
  const USER_ID = 'u_123';

  // Generate session ID
  const generateSessionId = () => {
    return `s_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  };

  // On mount, generate session id
  useEffect(() => {
    const newSessionId = generateSessionId();
    setSessionId(newSessionId);
    // eslint-disable-next-line
  }, []);

  // Create backend session (API call)
  const createSession = async (initialState = {}) => {
    try {
      const response = await fetch(
        `${API_BASE_URL}/apps/${APP_NAME}/users/${USER_ID}/sessions/${sessionId}`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
          mode: 'cors',
          credentials: 'include',
          body: JSON.stringify({
            state: {
              conversationStarted: true,
              language: selectedLanguage,
              timestamp: new Date().toISOString(),
              ...initialState
            }
          })
        }
      );
      if (!response.ok) throw new Error(await response.text());
      return await response.json();
    } catch (error) {
      return null;
    }
  };

  localStorage.setItem("sessionId", sessionId);

  // Markdown conversion helper
  const convertMarkdownData = (text) => (
    <ReactMarkdown>{text}</ReactMarkdown>
  );

  // Convert file to base64
  const fileToBase64 = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        const base64 = reader.result.split(',')[1];
        resolve(base64);
      };
      reader.onerror = error => reject(error);
    });
  };

  // Handle image select
  const handleImageSelect = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (!file.type.startsWith('image/')) {
        alert('Please select an image file');
        return;
      }
      if (file.size > 5 * 1024 * 1024) {
        alert('Image size should be less than 5MB');
        return;
      }
      setSelectedImage(file);
      const reader = new FileReader();
      reader.onload = (e) => setImagePreview(e.target.result);
      reader.readAsDataURL(file);
    }
  };

  // Remove image
  const removeImage = () => {
    setSelectedImage(null);
    setImagePreview(null);
    if (fileInputRef.current) fileInputRef.current.value = '';
  };

  // Send message API
  const sendMessageToAPI = async (message, imageFile = null) => {
    try {
      const messageParts = [];
      if (imageFile) {
        const base64Data = await fileToBase64(imageFile);
        messageParts.push({
          inline_data: {
            mime_type: imageFile.type,
            data: base64Data
          }
        });
      }
      if (message.trim()) {
        messageParts.push({ text: message });
      }
      const payload = {
        appName: APP_NAME,
        userId: USER_ID,
        sessionId: sessionId,
        newMessage: {
          role: "user",
          parts: messageParts
        }
      };
      const response = await fetch(`${API_BASE_URL}/run`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        mode: 'cors',
        credentials: 'include',
        body: JSON.stringify(payload)
      });
      if (!response.ok) throw new Error(await response.text());
      const responseData = await response.json();
      let n = responseData.length - 1;
      let res = responseData[n].content.parts[0].text;
      let result = convertMarkdownData(res);
      return result || "I received your message but couldn't process it properly. Please try again.";
    } catch (error) {
      if (error.message.includes('Failed to fetch') || error.message.includes('CORS')) {
        return "I'm having trouble connecting to the server. Please check if the API server is running and CORS is properly configured.";
      } else {
        return "I'm sorry, I encountered an error while processing your message. Please try again.";
      }
    }
  };

  // Test API connection
  const testAPIConnection = async () => {
    try {
      await sendMessageToAPI("Hello, this is a connection test");
    } catch (error) {}
  };

  // MAIN message send handler
  const handleSendMessage = async () => {
    if (!inputText.trim() && !selectedImage) return;
    setIsLoading(true);
    if (!hasStartedChat) {
      await createSession({
        firstMessage: inputText.trim() || 'Image message',
        hasImage: !!selectedImage
      });
    }
    const newMessage = {
      id: Date.now(),
      text: inputText || (selectedImage ? 'Sent an image' : ''),
      isUser: true,
      timestamp: new Date(),
      image: imagePreview
    };
    setMessages(prev => [...prev, newMessage]);
    const currentInput = inputText;
    const currentImage = selectedImage;
    setInputText('');
    removeImage();
    setHasStartedChat(true);
    try {
      const apiResponse = await sendMessageToAPI(currentInput, currentImage);
      const botResponse = {
        id: Date.now() + 1,
        text: apiResponse,
        isUser: false,
        timestamp: new Date()
      };
      setMessages(prev => [...prev, botResponse]);
    } catch (error) {
      const fallbackResponse = {
        id: Date.now() + 1,
        text: "I'm sorry, I'm having trouble connecting right now. Please try again later.",
        isUser: false,
        timestamp: new Date()
      };
      setMessages(prev => [...prev, fallbackResponse]);
    } finally {
      setIsLoading(false);
    }
  };

  // SPEECH RECOGNITION logic
  const handleStartListening = () => {
    setMicError('');
    setTranscript('');
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setMicError('Sorry, your browser does not support speech recognition.');
      return;
    }
    const recognition = new SpeechRecognition();
    recognition.lang = selectedLanguage === 'en' ? 'en-US' : selectedLanguage;
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    speechRecognitionRef.current = recognition;
    recognition.onstart = () => {
      setIsListening(true);
    };
    recognition.onresult = (event) => {
      if (event.results && event.results[0]) {
        setTranscript(event.results[0][0].transcript || '');
        setInputText(event.results[0][0].transcript || '');
      }
    };
    recognition.onerror = (event) => {
      setMicError(event.error || 'Microphone error. Please try again.');
      setIsListening(false);
    };
    recognition.onend = () => {
      setIsListening(false);
      // Send after result filled (transcript OR inputText updated)
      setTimeout(() => {
        setTranscript('');
        setMicError('');
        if (inputText.trim()) handleSendMessage();
      }, 500);
    };
    recognition.start();
    // 3s of silence = stop and trigger onend
    if (silenceTimeoutRef.current) clearTimeout(silenceTimeoutRef.current);
    silenceTimeoutRef.current = setTimeout(() => {
      if (speechRecognitionRef.current && isListening) {
        recognition.stop();
      }
    }, 3000);
  };

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (speechRecognitionRef.current) speechRecognitionRef.current.abort();
      if (silenceTimeoutRef.current) clearTimeout(silenceTimeoutRef.current);
    };
    // eslint-disable-next-line
  }, []);

  // Also assign handler for welcome screen
  const handleVoiceInput = handleStartListening;

  // Enter key press = Send
  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  // --- WELCOME SCREEN ---
  if (!hasStartedChat) {
    return (
      <div className="min-h-screen flex flex-col bg-white">
        {/* Header */}
        <header className="bg-white shadow-sm border-b border-gray-100 p-5 pt-12 flex items-center justify-between">
          <h1 className="text-xl font-bold text-gray-800">
            {getTranslation(selectedLanguage, 'appTitle')}
          </h1>
          <button className="p-2 hover:bg-gray-50 rounded-lg transition-colors">
            <Calendar className="h-6 w-6 text-gray-600" />
          </button>
        </header>
        {/* Main Content */}
        <main className="flex-grow flex flex-col items-center justify-center p-5">
          {/* Welcome Message */}
          <div className="text-center mb-16">
            <p className="text-2xl font-bold text-gray-800 leading-8">
              {getTranslation(selectedLanguage, 'welcome')}
            </p>
          </div>
          {/* Session Status Display */}
          <div className="mb-8 p-4 bg-blue-50 border border-blue-200 rounded-lg max-w-md">
            <p className="text-sm text-blue-700 mb-2">
              <strong>Session Information:</strong>
            </p>
            <p className="text-xs text-blue-600">
              Session ID: {sessionId || 'Generating...'}
            </p>
            <p className="text-xs text-blue-600">
              API Endpoint: {API_BASE_URL}/run
            </p>
            <p className="text-xs text-blue-600">
              App: {APP_NAME} | User: {USER_ID}
            </p>
            <div className="mt-3 flex flex-wrap gap-2">
              <button
                onClick={testAPIConnection}
                className="text-xs bg-blue-100 hover:bg-blue-200 text-blue-700 px-2 py-1 rounded"
                disabled={!sessionId}
              >
                Test API Connection
              </button>
              <button
                onClick={() => createSession({ manual: true })}
                className="text-xs bg-green-100 hover:bg-green-200 text-green-700 px-2 py-1 rounded"
                disabled={!sessionId}
              >
                Create Backend Session
              </button>
            </div>
          </div>
          {/* Mic Button */}
          <button
            onClick={handleVoiceInput}
            disabled={isListening || isLoading || !sessionId}
            className={`w-20 h-20 rounded-full flex items-center justify-center mb-12 shadow-lg transition-all duration-200 transform hover:scale-105 active:scale-95 ${
              isListening 
                ? 'bg-red-500 animate-pulse shadow-red-200' 
                : isLoading || !sessionId
                ? 'bg-gray-400 cursor-not-allowed'
                : 'bg-green-500 hover:bg-green-600 shadow-green-200'
            }`}
          >
            <Mic className="h-8 w-8 text-white" />
          </button>
          {isListening && (
            <p className="text-gray-600 mb-4 animate-pulse text-center">
              {getTranslation(selectedLanguage, 'listening')}
            </p>
          )}
          {micError && (
            <p className="text-red-600 mb-4 text-center text-sm animate-pulse">{micError}</p>
          )}
          {isLoading && (
            <p className="text-gray-600 mb-8 text-center">
              Processing your request...
            </p>
          )}
          {!sessionId && (
            <p className="text-gray-500 mb-8 text-center text-sm">
              Initializing session...
            </p>
          )}
        </main>
        {/* Bottom Input */}
        <div className="p-5 border-t border-gray-100">
          {/* Image Preview */}
          {imagePreview && (
            <div className="mb-3 relative inline-block">
              <img 
                src={imagePreview} 
                alt="Selected" 
                className="w-20 h-20 object-cover rounded-lg border-2 border-green-200"
              />
              <button
                onClick={removeImage}
                className="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs hover:bg-red-600"
              >
                <X className="w-3 h-3" />
              </button>
            </div>
          )}
          <div className="flex items-end bg-gray-50 rounded-3xl px-4 py-3 shadow-sm">
            <textarea
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder={sessionId ? getTranslation(selectedLanguage, 'enterText') : 'Initializing session...'}
              className="flex-1 bg-transparent outline-none text-gray-800 placeholder-gray-500 resize-none max-h-32 py-2"
              rows="1"
              disabled={isLoading || !sessionId}
            />
            {/* Mic in input bar */}
            <button
              disabled={isListening || isLoading || !sessionId}
              onClick={handleVoiceInput}
              type="button"
              aria-label={isListening ? "Listening..." : "Start voice input"}
              className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-110 active:scale-90
                ${isListening
                  ? 'bg-red-500 animate-pulse text-white shadow-red-200'
                  : (!isLoading && sessionId ? 'bg-green-500 hover:bg-green-600 text-white shadow-md' : 'bg-gray-300 text-gray-500 cursor-not-allowed')}`}
            >
              <Mic className="h-5 w-5" />
            </button>
            <input
              type="file"
              ref={fileInputRef}
              onChange={handleImageSelect}
              accept="image/*"
              className="hidden"
            />
            <button
              onClick={() => fileInputRef.current?.click()}
              disabled={isLoading || !sessionId}
              className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
                !isLoading && sessionId
                  ? 'bg-blue-500 hover:bg-blue-600 text-white shadow-md'
                  : 'bg-gray-300 text-gray-500 cursor-not-allowed'
              }`}
            >
              <ImageIcon className="h-5 w-5" />
            </button>
            <button
              onClick={handleSendMessage}
              disabled={(!inputText.trim() && !selectedImage) || isLoading || !sessionId}
              className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
                (inputText.trim() || selectedImage) && !isLoading && sessionId
                  ? 'bg-green-500 hover:bg-green-600 text-white shadow-md'
                  : 'bg-gray-300 text-gray-500 cursor-not-allowed'
              }`}
            >
              {isLoading ? (
                <div className="h-5 w-5 border-2 border-gray-400 border-t-transparent rounded-full animate-spin" />
              ) : (
                <Send className="h-5 w-5" />
              )}
            </button>
          </div>
        </div>
      </div>
    );
  }

  // --- MAIN CHAT UI ---
  return (
    <div className="min-h-screen flex flex-col bg-white">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-100 p-5 pt-12 flex items-center justify-between">
        <h1 className="text-xl font-bold text-gray-800">
          {getTranslation(selectedLanguage, 'appTitle')}
        </h1>
        <div className="flex items-center space-x-3">
          {sessionId && (
            <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
              Session: {sessionId.slice(-8)}
            </span>
          )}
          <button className="p-2 hover:bg-gray-50 rounded-lg transition-colors">
            <Calendar className="h-6 w-6 text-gray-600" />
          </button>
        </div>
      </header>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-5 space-y-4">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${message.isUser ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-xs lg:max-w-md px-4 py-3 rounded-2xl ${
                message.isUser
                  ? 'bg-green-500 text-white rounded-br-md'
                  : 'bg-gray-100 text-gray-800 rounded-bl-md'
              }`}
            >
              {message.image && (
                <img 
                  src={message.image} 
                  alt="Sent image" 
                  className="w-full max-w-48 h-auto rounded-lg mb-2"
                />
              )}
              <div className="text-sm leading-6">{message.text}</div>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-gray-100 text-gray-800 rounded-2xl rounded-bl-md px-4 py-3">
              <div className="flex space-x-1">
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
              </div>
            </div>
          </div>
        )}
      </div>
      {/* Input Container with Mic */}
      <div className="p-5 border-t border-gray-100">
        {imagePreview && (
          <div className="mb-3 relative inline-block">
            <img 
              src={imagePreview} 
              alt="Selected" 
              className="w-20 h-20 object-cover rounded-lg border-2 border-green-200"
            />
            <button
              onClick={removeImage}
              className="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs hover:bg-red-600"
            >
              <X className="w-3 h-3" />
            </button>
          </div>
        )}
        <div className="flex items-end bg-gray-50 rounded-3xl px-4 py-3 shadow-sm">
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your message..."
            className="flex-1 bg-transparent outline-none text-gray-800 placeholder-gray-500 resize-none max-h-32 py-2"
            rows="1"
            disabled={isLoading}
            style={{ minWidth: 0 }}
          />
          {/* Mic Button (on input bar) */}
          <button
            disabled={isListening || isLoading}
            onClick={handleStartListening}
            type="button"
            aria-label={isListening ? "Listening..." : "Start voice input"}
            className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-110 active:scale-90
              ${isListening
                ? 'bg-red-500 animate-pulse text-white shadow-red-200'
                : (!isLoading ? 'bg-green-500 hover:bg-green-600 text-white shadow-md' : 'bg-gray-300 text-gray-500 cursor-not-allowed')}`}
          >
            <Mic className="h-5 w-5" />
          </button>
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleImageSelect}
            accept="image/*"
            className="hidden"
          />
          <button
            onClick={() => fileInputRef.current?.click()}
            disabled={isLoading}
            className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
              !isLoading
                ? 'bg-blue-500 hover:bg-blue-600 text-white shadow-md'
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
          >
            <ImageIcon className="h-5 w-5" />
          </button>
          <button
            onClick={handleSendMessage}
            disabled={(!inputText.trim() && !selectedImage) || isLoading}
            className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
              (inputText.trim() || selectedImage) && !isLoading
                ? 'bg-green-500 hover:bg-green-600 text-white shadow-md'
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
          >
            {isLoading ? (
              <div className="h-5 w-5 border-2 border-gray-400 border-t-transparent rounded-full animate-spin" />
            ) : (
              <Send className="h-5 w-5" />
            )}
          </button>
        </div>
        {/* Mic status and errors */}
        {isListening && (
          <p className="text-gray-600 mt-2 animate-pulse text-center">
            {getTranslation(selectedLanguage, 'listening')}
          </p>
        )}
        {micError && (
          <p className="text-red-600 mt-2 text-center text-sm animate-pulse">{micError}</p>
        )}
      </div>
    </div>
  );
};

export default Home;
