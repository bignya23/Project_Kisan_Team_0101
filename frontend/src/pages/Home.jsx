import React, { useState, useEffect, useRef } from 'react';
import { Calendar, Mic, Send, ImageIcon, X, Camera } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

// Mock store and translation function for demo
const useAppStore = () => ({
  selectedLanguage: 'en',
  location
});
 //console.log(location)
const getTranslation = (lang, key) => {
  const translations = {
    appTitle: 'Project Kisan',
    welcome: 'Welcome to Project Kisan! How can I help you today?',
    enterText: 'Type your question here...',
    ask: 'Ask',
    listening: 'Listening... Speak now',
    takePhoto: 'Take Photo',
    uploadImage: 'Upload Image'
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
  const [cameraStream, setCameraStream] = useState(null);
  const [showCamera, setShowCamera] = useState(false);
  const [isImageRequired, setIsImageRequired] = useState(false);
  const [isVoiceInput, setIsVoiceInput] = useState(false);
  const [isPlayingAudio, setIsPlayingAudio] = useState(false);
  
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const speechRecognitionRef = useRef(null);
  const silenceTimeoutRef = useRef(null);
  const fileInputRef = useRef(null);
  const audioRef = useRef(null);

  // API Configuration
  const API_BASE_URL = window.location.hostname.includes('cloudworkstations.dev') 
    ? `https://${window.location.hostname.replace('5174-', '8000-')}`
    : 'https://capital-agent-new-159735707573.us-central1.run.app';
  const APP_NAME = 'capital_agent';
  const USER_ID = 'u_1234';

  // Initialize audio ref
  useEffect(() => {
    audioRef.current = new Audio("/assets/male_output.mp3");
    audioRef.current.onplay = () => setIsPlayingAudio(true);
    audioRef.current.onended = () => setIsPlayingAudio(false);
    audioRef.current.onerror = () => setIsPlayingAudio(false);
    
    return () => {
      if (audioRef.current) {
        audioRef.current.pause();
        audioRef.current = null;
      }
    };
  }, []);

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

  // Cleanup camera stream on unmount
  useEffect(() => {
    return () => {
      if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
      }
    };
  }, [cameraStream]);

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
      console.log(response);
      return await response.json();
    } catch (error) {
      return null;
    }
    
  };

  const checkImageProvideRequest = (text) => {
    const lowerText = text.toLowerCase().trim();
    const phrasesToCheck = [
      /(provide|share|upload|send|attach)\s+(a\s+)?(photo|image|picture)/,
      /(need|want|require)\s+(a\s+)?(photo|image|picture)/,
      /(can you|could you|would you)\s+(provide|share|upload|send|attach)\s+(a\s+)?(photo|image|picture)/,
      /(do you have|can i see|can you show)\s+(a\s+)?(photo|image|picture)/,
      /^(please\s+)?(provide|share|upload|send|attach)\s+(a\s+)?(photo|image|picture)/,
      /(I'd like to|I need to|I want to)\s+(share|upload|send|attach)\s+(a\s+)?(photo|image|picture)/,
      /(show me|send me)\s+(a\s+)?(photo|image|picture)/
    ];
  
    const isImageRequested = phrasesToCheck.some(regex => regex.test(lowerText));
  
    if (isImageRequested) {
      console.log("🟢 Detected a request for photo/image:", lowerText);
      setIsImageRequired(true);
    } else {
      console.log("🔴 No photo/image request found in:", lowerText);
      setIsImageRequired(false);
    }
  };

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

  // Handle image select from gallery
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

  // Start camera
  const startCamera = async () => {
    try {
      setShowCamera(true);
      const stream = await navigator.mediaDevices.getUserMedia({ 
        video: { facingMode: 'environment' },
        audio: false 
      });
      setCameraStream(stream);
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
      }
    } catch (err) {
      console.error("Error accessing camera:", err);
      alert("Could not access the camera. Please check permissions.");
      setShowCamera(false);
    }
  };

  // Stop camera
  const stopCamera = () => {
    if (cameraStream) {
      cameraStream.getTracks().forEach(track => track.stop());
      setCameraStream(null);
    }
    setShowCamera(false);
  };

  // Capture photo from camera
  const capturePhoto = () => {
    if (videoRef.current && canvasRef.current) {
      const video = videoRef.current;
      const canvas = canvasRef.current;
      const context = canvas.getContext('2d');
      
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
      
      canvas.toBlob((blob) => {
        if (blob) {
          const file = new File([blob], 'captured-photo.jpg', { type: 'image/jpeg' });
          setSelectedImage(file);
          setImagePreview(URL.createObjectURL(blob));
          stopCamera();
        }
      }, 'image/jpeg', 0.9);
    }
  };

  // Remove image
  const removeImage = () => {
    setSelectedImage(null);
    setImagePreview(null);
    if (fileInputRef.current) fileInputRef.current.value = '';
  };

  // Play audio response
  const playAudioResponse = () => {
    if (audioRef.current) {
      audioRef.current.play().catch(error => {
        console.error("Audio playback error:", error);
        setIsPlayingAudio(false);
      });
    }
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


    //   curl -X POST -H "Authorization: Bearer $TOKEN" \
    // $APP_URL/run_sse \
    // -H "Content-Type: application/json" \
    // -d '{
    // "app_name": "capital_agent",
    // "user_id": "user_123",
    // "session_id": "session_abc",
    // "new_message": {
    //     "role": "user",
    //     "parts": [{
    //     "text": "What is the capital of Canada?"
    //     }]
    // },
    // "streaming": false
    // }'
      const response = await fetch(`${API_BASE_URL}/run`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
      });
      if (!response.ok) throw new Error(await response.text());
      console.log(response);
      const responseData = await response.json();
      let n = responseData.length - 1;
      let res = responseData[n].content.parts[0].text;
      let result = convertMarkdownData(res);
      checkImageProvideRequest(res);
      
      // Play audio for voice responses
      if (isVoiceInput) {
        playAudioResponse();
      }
      
      return result || "I received your message but couldn't process it properly. Please try again.";
    } catch (error) {
      if (error.message.includes('Failed to fetch') || error.message.includes('CORS')) {
        return "I'm having trouble connecting to the server. Please check if the API server is running and CORS is properly configured.";
      } else {
        return "I'm sorry, I encountered an error while processing your message. Please try again.";
      }
    }
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
    let currentInput = inputText;
    if (isVoiceInput && inputText.trim()) {
      currentInput = currentInput + " " + "is_audio = True";
    }
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
      setIsVoiceInput(false);
    }
  };

  // Auto-send voice input when silence is detected
  const handleAutoSendVoiceInput = async () => {
    if (isVoiceInput && inputText.trim()) {
      await handleSendMessage();
    }
  };

  // SPEECH RECOGNITION logic
  const handleStartListening = () => {
    setMicError('');
    setTranscript('');
    setIsVoiceInput(true);
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
        const newTranscript = event.results[0][0].transcript || '';
        setTranscript(newTranscript);
        setInputText(newTranscript);
      }
    };
    recognition.onerror = (event) => {
      setMicError(event.error || 'Microphone error. Please try again.');
      setIsListening(false);
      setIsVoiceInput(false);
    };
    recognition.onend = () => {
      setIsListening(false);
      setTimeout(handleAutoSendVoiceInput, 500);
    };
    recognition.start();
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
      if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
      }
      if (audioRef.current) {
        audioRef.current.pause();
      }
    };
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
      <div className="min-h-screen flex flex-col bg-gradient-to-b from-green-50 to-white">
        {/* Header */}
        <header className="bg-white shadow-sm border-b border-green-100 p-5 pt-12 flex items-center justify-between">
          <h1 className="text-xl font-bold text-green-800">
            {getTranslation(selectedLanguage, 'appTitle')}
          </h1>
          <button className="p-2 hover:bg-green-50 rounded-lg transition-colors">
            <Calendar className="h-6 w-6 text-green-600" />
          </button>
        </header>

        {/* Camera Modal */}
        {showCamera && (
          <div className="fixed inset-0 bg-black bg-opacity-75 z-50 flex flex-col items-center justify-center p-4">
            <div className="relative w-full max-w-md">
              <video 
                ref={videoRef} 
                autoPlay 
                playsInline 
                className="w-full h-auto rounded-lg"
              />
              <canvas ref={canvasRef} className="hidden" />
              <div className="flex justify-center space-x-4 mt-4">
                <button
                  onClick={capturePhoto}
                  className="w-16 h-16 rounded-full bg-red-500 border-4 border-white flex items-center justify-center shadow-lg"
                >
                  <Camera className="h-8 w-8 text-white" />
                </button>
                <button
                  onClick={stopCamera}
                  className="w-12 h-12 rounded-full bg-gray-600 text-white flex items-center justify-center"
                >
                  <X className="h-6 w-6" />
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Main Content */}
        <main className="flex-grow flex flex-col items-center justify-center p-5">
          {/* Welcome Message */}
          <div className="text-center mb-16">
            <p className="text-2xl font-bold text-green-800 leading-8">
              {getTranslation(selectedLanguage, 'welcome')}
            </p>
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
                : 'bg-green-600 hover:bg-green-700 shadow-green-200'
            }`}
          >
            <Mic className="h-8 w-8 text-white" />
          </button>
          {isListening && (
            <p className="text-green-700 mb-4 animate-pulse text-center">
              {getTranslation(selectedLanguage, 'listening')}
            </p>
          )}
          {micError && (
            <p className="text-red-600 mb-4 text-center text-sm animate-pulse">{micError}</p>
          )}
          {isLoading && (
            <p className="text-green-700 mb-8 text-center">
              Processing your request...
            </p>
          )}
          {!sessionId && (
            <p className="text-green-600 mb-8 text-center text-sm">
              Initializing session...
            </p>
          )}
        </main>

        {/* Bottom Input */}
        <div className="p-5 border-t border-green-100 bg-white">
          {/* Image Preview */}
          {imagePreview && (
            <div className="mb-3 relative inline-block">
              <img 
                src={imagePreview} 
                alt="Selected" 
                className="w-20 h-20 object-cover rounded-lg border-2 border-green-300"
              />
              <button
                onClick={removeImage}
                className="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs hover:bg-red-600"
              >
                <X className="w-3 h-3" />
              </button>
            </div>
          )}
          <div className="flex items-end bg-green-50 rounded-3xl px-4 py-3 shadow-sm border border-green-100">
            <textarea
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder={sessionId ? getTranslation(selectedLanguage, 'enterText') : 'Initializing session...'}
              className="flex-1 bg-transparent outline-none text-green-900 placeholder-green-500 resize-none max-h-32 py-2"
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
                  : (!isLoading && sessionId ? 'bg-green-600 hover:bg-green-700 text-white shadow-md' : 'bg-gray-300 text-gray-500 cursor-not-allowed')}`}
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
                  ? 'bg-green-500 hover:bg-green-600 text-white shadow-md'
                  : 'bg-gray-300 text-gray-500 cursor-not-allowed'
              }`}
            >
              <ImageIcon className="h-5 w-5" />
            </button>
            <button
              onClick={startCamera}
              disabled={isLoading || !sessionId}
              className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
                !isLoading && sessionId
                  ? 'bg-blue-500 hover:bg-blue-600 text-white shadow-md'
                  : 'bg-gray-300 text-gray-500 cursor-not-allowed'
              }`}
            >
              <Camera className="h-5 w-5" />
            </button>
            <button
              onClick={handleSendMessage}
              disabled={(!inputText.trim() && !selectedImage) || isLoading || !sessionId}
              className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
                (inputText.trim() || selectedImage) && !isLoading && sessionId
                  ? 'bg-green-600 hover:bg-green-700 text-white shadow-md'
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
    <div className="min-h-screen flex flex-col bg-gradient-to-b from-green-50 to-white">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-green-100 p-5 pt-12 flex items-center justify-between">
        <h1 className="text-xl font-bold text-green-800">
          {getTranslation(selectedLanguage, 'appTitle')}
        </h1>
        <div className="flex items-center space-x-3">
          {sessionId && (
            <span className="text-xs text-green-700 bg-green-100 px-2 py-1 rounded">
              Session: {sessionId.slice(-8)}
            </span>
          )}
          <button className="p-2 hover:bg-green-50 rounded-lg transition-colors">
            <Calendar className="h-6 w-6 text-green-600" />
          </button>
        </div>
      </header>

      {/* Camera Modal */}
      {showCamera && (
        <div className="fixed inset-0 bg-black bg-opacity-75 z-50 flex flex-col items-center justify-center p-4">
          <div className="relative w-full max-w-md">
            <video 
              ref={videoRef} 
              autoPlay 
              playsInline 
              className="w-full h-auto rounded-lg"
            />
            <canvas ref={canvasRef} className="hidden" />
            <div className="flex justify-center space-x-4 mt-4">
              <button
                onClick={capturePhoto}
                className="w-16 h-16 rounded-full bg-red-500 border-4 border-white flex items-center justify-center shadow-lg"
              >
                <Camera className="h-8 w-8 text-white" />
              </button>
              <button
                onClick={stopCamera}
                className="w-12 h-12 rounded-full bg-gray-600 text-white flex items-center justify-center"
              >
                <X className="h-6 w-6" />
              </button>
            </div>
          </div>
        </div>
      )}

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
                  ? 'bg-green-600 text-white rounded-br-md shadow-md'
                  : 'bg-white text-gray-800 rounded-bl-md shadow-md border border-green-100'
              }`}
            >
              {message.image && (
                <img 
                  src={message.image} 
                  alt="Sent image" 
                  className="w-full max-w-48 h-auto rounded-lg mb-2"
                />
              )}
              <div className="text-sm leading-6">
                {message.text}
                {!message.isUser && isPlayingAudio && messages[messages.length - 1].id === message.id && (
                  <div className="flex items-center mt-2 text-green-600">
                    <div className="flex space-x-1">
                      <div className="w-2 h-2 bg-green-400 rounded-full animate-bounce"></div>
                      <div className="w-2 h-2 bg-green-500 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                      <div className="w-2 h-2 bg-green-600 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                    </div>
                    <span className="ml-2 text-xs">Playing audio...</span>
                  </div>
                )}
              </div>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-white text-gray-800 rounded-2xl rounded-bl-md px-4 py-3 shadow-md border border-green-100">
              <div className="flex space-x-1">
                <div className="w-2 h-2 bg-green-400 rounded-full animate-bounce"></div>
                <div className="w-2 h-2 bg-green-500 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                <div className="w-2 h-2 bg-green-600 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Image Required Prompt */}
      {isImageRequired && (
        <div className="bg-yellow-50 border-t border-yellow-200 p-4">
          <div className="flex flex-col items-center space-y-3">
            <p className="text-yellow-800 text-sm font-medium text-center">
              Please provide an image as requested:
            </p>
            <div className="flex space-x-3">
              <button
                onClick={startCamera}
                className="flex items-center justify-center px-4 py-2 bg-green-600 text-white rounded-lg shadow hover:bg-green-700 transition-colors"
              >
                <Camera className="h-5 w-5 mr-2" />
                {getTranslation(selectedLanguage, 'takePhoto')}
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
                className="flex items-center justify-center px-4 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition-colors"
              >
                <ImageIcon className="h-5 w-5 mr-2" />
                {getTranslation(selectedLanguage, 'uploadImage')}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Input Container with Mic */}
      <div className="p-5 border-t border-green-100 bg-white">
        {imagePreview && (
          <div className="mb-3 relative inline-block">
            <img 
              src={imagePreview} 
              alt="Selected" 
              className="w-20 h-20 object-cover rounded-lg border-2 border-green-300"
            />
            <button
              onClick={removeImage}
              className="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs hover:bg-red-600"
            >
              <X className="w-3 h-3" />
            </button>
          </div>
        )}
        <div className="flex items-end bg-green-50 rounded-3xl px-4 py-3 shadow-sm border border-green-100">
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your message..."
            className="flex-1 bg-transparent outline-none text-green-900 placeholder-green-500 resize-none max-h-32 py-2"
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
                : (!isLoading ? 'bg-green-600 hover:bg-green-700 text-white shadow-md' : 'bg-gray-300 text-gray-500 cursor-not-allowed')}`}
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
                ? 'bg-green-500 hover:bg-green-600 text-white shadow-md'
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
          >
            <ImageIcon className="h-5 w-5" />
          </button>
          <button
            onClick={startCamera}
            disabled={isLoading}
            className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
              !isLoading
                ? 'bg-blue-500 hover:bg-blue-600 text-white shadow-md'
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
          >
            <Camera className="h-5 w-5" />
          </button>
          <button
            onClick={handleSendMessage}
            disabled={(!inputText.trim() && !selectedImage) || isLoading}
            className={`ml-2 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
              (inputText.trim() || selectedImage) && !isLoading
                ? 'bg-green-600 hover:bg-green-700 text-white shadow-md'
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
          <p className="text-green-700 mt-2 animate-pulse text-center">
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
