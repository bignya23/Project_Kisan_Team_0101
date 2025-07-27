import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, Send, User, Bot, Camera, Upload, X } from 'lucide-react';

// Mock store for demo
const useAppStore = () => ({
  user: { name: 'Demo User' },
  selectedLanguage: 'en'
});

const VoiceInput = () => {
  const { user, selectedLanguage } = useAppStore();
  const [isRecording, setIsRecording] = useState(false);
  const [voiceLevel, setVoiceLevel] = useState(0);
  const [showCamera, setShowCamera] = useState(false);
  const [stream, setStream] = useState(null);
  const [currentMessageId, setCurrentMessageId] = useState(null);
  const [sessionId, setSessionId] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [micError, setMicError] = useState('');
  const [transcript, setTranscript] = useState('');
  const speechRecognitionRef = useRef(null);
  const silenceTimeoutRef = useRef(null);
  
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'ai',
      text: 'Hello! I\'m your AI farming assistant. You can ask me anything about crops, diseases, weather, or farming techniques. Tap the microphone to start speaking!',
      timestamp: new Date()
    }
  ]);

  const demoQueries = [
    "What's wrong with my tomato plants?",
    "When should I plant rice?",
    "How to prevent pest attacks?",
    "Best fertilizer for wheat crop?"
  ];

  // API Configuration
  const API_BASE_URL = window.location.hostname.includes('cloudworkstations.dev') 
    ? `https://${window.location.hostname.replace('5173-', '8000-')}`
    : 'http://localhost:8000';
  const APP_NAME = 'kisan_agent';
  const USER_ID = 'u_123';

//   // Generate session ID
//   const generateSessionId = () => {
//     return `s_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
//   };

//   // On mount, generate session id
//   useEffect(() => {
//     const newSessionId = generateSessionId();
//     setSessionId(newSessionId);
//   }, []);

//   // Create backend session
//   const createSession = async (initialState = {}) => {
//     try {
//       const response = await fetch(
//         `${API_BASE_URL}/apps/${APP_NAME}/users/${USER_ID}/sessions/${sessionId}`,
//         {
//           method: 'POST',
//           headers: {
//             'Content-Type': 'application/json',
//             'Accept': 'application/json',
//           },
//           mode: 'cors',
//           credentials: 'include',
//           body: JSON.stringify({
//             state: {
//               conversationStarted: true,
//               language: selectedLanguage,
//               timestamp: new Date().toISOString(),
//               ...initialState
//             }
//           })
//         }
//       );
//       if (!response.ok) throw new Error(await response.text());
//       return await response.json();
//     } catch (error) {
//       console.error('Session creation failed:', error);
//       return null;
//     }
//   };

   const value = localStorage.getItem("sessionId");
   if(value){
    setSessionId(value);
   }


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

  // Check if message requests photo
  const checkImageProvideRequest = (text) => {
    const lowerText = text.toLowerCase();
    const parts = lowerText.split(" ");
    const provideIndex = parts.indexOf("provide");
    const photoIndex = parts.indexOf("photo");
    if (provideIndex !== -1 && photoIndex !== -1 && photoIndex === provideIndex + 1) {
      console.log("🟢 Detected a request to provide a photo.");
      return true;
    } else {
      console.log("🔴 No request to provide a photo found.");
      return false;
    }
  };

  // Send message to API
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
      
      // Check if response requests image
      const isImageProvide = checkImageProvideRequest(res);
      
      return {
        text: res,
        isImageProvide: isImageProvide
      };
    } catch (error) {
      console.error('API Error:', error);
      if (error.message.includes('Failed to fetch') || error.message.includes('CORS')) {
        return {
          text: "I'm having trouble connecting to the server. Please check if the API server is running and CORS is properly configured.",
          isImageProvide: false
        };
      } else {
        return {
          text: "I'm sorry, I encountered an error while processing your message. Please try again.",
          isImageProvide: false
        };
      }
    }
  };

  // Simulate voice level animation when recording
  useEffect(() => {
    let interval;
    if (isRecording) {
      interval = setInterval(() => {
        // Simulate varying voice levels (0-100)
        setVoiceLevel(Math.random() * 100);
      }, 150);
    } else {
      setVoiceLevel(0);
    }
    
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [isRecording]);

  // Speech Recognition Setup
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
      setIsRecording(true);
    };

    recognition.onresult = (event) => {
      if (event.results && event.results[0]) {
        const transcriptText = event.results[0][0].transcript || '';
        setTranscript(transcriptText);
        handleVoiceQuery(transcriptText);
      }
    };

    recognition.onerror = (event) => {
      setMicError(event.error || 'Microphone error. Please try again.');
      setIsRecording(false);
    };

    recognition.onend = () => {
      setIsRecording(false);
      setTimeout(() => {
        setTranscript('');
        setMicError('');
      }, 500);
    };

    recognition.start();

    // Auto-stop after 10 seconds of silence
    if (silenceTimeoutRef.current) clearTimeout(silenceTimeoutRef.current);
    silenceTimeoutRef.current = setTimeout(() => {
      if (speechRecognitionRef.current && isRecording) {
        recognition.stop();
      }
    }, 10000);
  };

  const handleMicPress = () => {
    if (isRecording) {
      // Stop recording
      if (speechRecognitionRef.current) {
        speechRecognitionRef.current.stop();
      }
      setIsRecording(false);
    } else {
      // Start recording
      handleStartListening();
    }
  };

  const handleDemoQuery = async (query) => {
    // if (!sessionId) {
    //   await createSession({ firstMessage: query });
    // }

    const userMessage = {
      id: Date.now(),
      sender: 'user',
      text: query,
      timestamp: new Date()
    };
    
    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    
    try {
      const apiResponse = await sendMessageToAPI(query);
      
      const aiResponse = {
        id: Date.now() + 1,
        sender: 'ai',
        text: apiResponse.text,
        timestamp: new Date(),
        showFileChooser: apiResponse.isImageProvide
      };
      setMessages(prev => [...prev, aiResponse]);
    } catch (error) {
      const fallbackResponse = {
        id: Date.now() + 1,
        sender: 'ai',
        text: "I'm sorry, I'm having trouble connecting right now. Please try again later.",
        timestamp: new Date()
      };
      setMessages(prev => [...prev, fallbackResponse]);
    } finally {
      setIsLoading(false);
    }
  };

  const startCamera = async (messageId) => {
    try {
      setCurrentMessageId(messageId);
      const mediaStream = await navigator.mediaDevices.getUserMedia({ 
        video: { 
          facingMode: 'environment' // Prefer rear camera
        } 
      });
      setStream(mediaStream);
      setShowCamera(true);
    } catch (error) {
      console.error('Error accessing camera:', error);
      alert('Unable to access camera. Please check permissions or use file upload instead.');
    }
  };

  const stopCamera = () => {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      setStream(null);
    }
    setShowCamera(false);
    setCurrentMessageId(null);
  };

  const capturePhoto = () => {
    const video = document.getElementById('camera-video');
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0);
    
    canvas.toBlob((blob) => {
      const file = new File([blob], `photo-${Date.now()}.jpg`, { type: 'image/jpeg' });
      handlePhotoCapture(file, currentMessageId);
    }, 'image/jpeg', 0.8);
  };

  const handlePhotoCapture = async (file, messageId) => {
    // Update the message to show photo was taken
    setMessages(prev => prev.map(msg => 
      msg.id === messageId 
        ? { ...msg, selectedFile: `📷 ${file.name}`, showFileChooser: false }
        : msg
    ));
    
    stopCamera();
    setIsLoading(true);
    
    try {
      const apiResponse = await sendMessageToAPI('', file);
      
      const aiResponse = {
        id: Date.now() + 1,
        sender: 'ai',
        text: apiResponse.text,
        timestamp: new Date(),
        showFileChooser: apiResponse.isImageProvide
      };
      setMessages(prev => [...prev, aiResponse]);
    } catch (error) {
      const fallbackResponse = {
        id: Date.now() + 1,
        sender: 'ai',
        text: "I'm sorry, I'm having trouble analyzing your photo right now. Please try again later.",
        timestamp: new Date()
      };
      setMessages(prev => [...prev, fallbackResponse]);
    } finally {
      setIsLoading(false);
    }
  };

  // Effect to handle camera stream
  useEffect(() => {
    if (showCamera && stream) {
      const video = document.getElementById('camera-video');
      if (video) {
        video.srcObject = stream;
      }
    }
  }, [showCamera, stream]);

  // Cleanup camera on unmount
  useEffect(() => {
    return () => {
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
      }
      if (speechRecognitionRef.current) speechRecognitionRef.current.abort();
      if (silenceTimeoutRef.current) clearTimeout(silenceTimeoutRef.current);
    };
  }, [stream]);

  const handleFileUpload = async (event, messageId) => {
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

      // Update the message to show file was selected
      setMessages(prev => prev.map(msg => 
        msg.id === messageId 
          ? { ...msg, selectedFile: file.name, showFileChooser: false }
          : msg
      ));
      
      setIsLoading(true);
      
      try {
        const apiResponse = await sendMessageToAPI('', file);
        
        const aiResponse = {
          id: Date.now() + 1,
          sender: 'ai',
          text: apiResponse.text,
          timestamp: new Date(),
          showFileChooser: apiResponse.isImageProvide
        };
        setMessages(prev => [...prev, aiResponse]);
      } catch (error) {
        const fallbackResponse = {
          id: Date.now() + 1,
          sender: 'ai',
          text: "I'm sorry, I'm having trouble analyzing your image right now. Please try again later.",
          timestamp: new Date()
        };
        setMessages(prev => [...prev, fallbackResponse]);
      } finally {
        setIsLoading(false);
      }
    }
  };

  const handleVoiceQuery = async (transcribedText) => {
    if (!sessionId) {
      await createSession({ firstMessage: transcribedText, isVoice: true });
    }

    const userMessage = {
      id: Date.now(),
      sender: 'user',
      text: transcribedText,
      timestamp: new Date(),
      isVoice: true
    };
    
    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    
    try {
      const apiResponse = await sendMessageToAPI(transcribedText);
      
      const aiResponse = {
        id: Date.now() + 1,
        sender: 'ai',
        text: apiResponse.text,
        timestamp: new Date(),
        showFileChooser: apiResponse.isImageProvide
      };
      setMessages(prev => [...prev, aiResponse]);
    } catch (error) {
      const fallbackResponse = {
        id: Date.now() + 1,
        sender: 'ai',
        text: "I'm sorry, I'm having trouble processing your voice message right now. Please try again later.",
        timestamp: new Date()
      };
      setMessages(prev => [...prev, fallbackResponse]);
    } finally {
      setIsLoading(false);
    }
  };

  // Sound wave bars component
  const SoundWaves = ({ isActive, level }) => {
    const bars = [
      { height: Math.max(20, (level * 0.4) + 10), delay: '0ms' },
      { height: Math.max(15, (level * 0.6) + 8), delay: '100ms' },
      { height: Math.max(25, (level * 0.8) + 12), delay: '200ms' },
      { height: Math.max(18, (level * 0.5) + 9), delay: '150ms' },
      { height: Math.max(22, (level * 0.7) + 11), delay: '50ms' }
    ];

    return (
      <div className="flex items-center justify-center space-x-1">
        {bars.map((bar, index) => (
          <div
            key={index}
            className={`w-1 bg-white rounded-full transition-all duration-150 ${
              isActive ? 'opacity-100' : 'opacity-30'
            }`}
            style={{
              height: isActive ? `${bar.height}px` : '12px',
              animationDelay: bar.delay
            }}
          />
        ))}
      </div>
    );
  };

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b p-4">
        <h1 className="text-xl font-semibold text-gray-900">Voice Assistant</h1>
        <p className="text-sm text-gray-600">Speak naturally, get instant farming advice</p>
        {sessionId && (
          <p className="text-xs text-gray-500 mt-1">Session: {sessionId.slice(-8)}</p>
        )}
      </div>

      {/* Demo Cards */}
      {messages.length <= 1 && (
        <div className="p-4">
          <h3 className="text-sm font-medium text-gray-700 mb-3">Try asking:</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
            {demoQueries.map((query, index) => (
              <button
                key={index}
                onClick={() => handleDemoQuery(query)}
                disabled={isLoading}
                className="text-left p-3 bg-white rounded-lg border border-gray-200 hover:border-green-300 hover:bg-green-50 transition-colors text-sm disabled:opacity-50 disabled:cursor-not-allowed"
              >
                "{query}"
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`flex items-start space-x-2 max-w-xs lg:max-w-md ${
                message.sender === 'user' ? 'flex-row-reverse space-x-reverse' : ''
              }`}
            >
              <div
                className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
                  message.sender === 'user' 
                    ? 'bg-green-500 text-white' 
                    : 'bg-blue-500 text-white'
                }`}
              >
                {message.sender === 'user' ? (
                  <User className="h-4 w-4" />
                ) : (
                  <Bot className="h-4 w-4" />
                )}
              </div>
              <div
                className={`px-4 py-2 rounded-lg ${
                  message.sender === 'user'
                    ? 'bg-green-500 text-white'
                    : 'bg-white text-gray-900 border border-gray-200'
                }`}
              >
                <p className="text-sm">{message.text}</p>
                {message.isVoice && (
                  <span className="text-xs opacity-75 mt-1 block">🎤 Voice message</span>
                )}
                {message.selectedFile && (
                  <span className="text-xs opacity-75 mt-1 block">📎 {message.selectedFile}</span>
                )}
                {message?.showFileChooser && (
                  <div className="mt-3 p-3 bg-gray-50 rounded-lg border-2 border-dashed border-gray-300">
                    <div className="space-y-3">
                      <p className="text-xs text-gray-600 font-medium">Share an image of your crop:</p>
                      
                      {/* Camera Capture */}
                      <div className="relative">
                        <button
                          onClick={() => startCamera(message.id)}
                          disabled={isLoading}
                          className="flex items-center justify-center w-full p-3 bg-blue-50 border-2 border-blue-200 border-dashed rounded-lg cursor-pointer hover:bg-blue-100 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                          <Camera className="h-5 w-5 text-blue-600 mr-2" />
                          <span className="text-sm font-medium text-blue-700">Take Photo</span>
                        </button>
                      </div>

                      {/* File Upload */}
                      <div className="relative">
                        <input
                          type="file"
                          accept="image/*"
                          onChange={(e) => handleFileUpload(e, message.id)}
                          className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                          id={`file-${message.id}`}
                          disabled={isLoading}
                        />
                        <label
                          htmlFor={`file-${message.id}`}
                          className={`flex items-center justify-center w-full p-3 bg-green-50 border-2 border-green-200 border-dashed rounded-lg cursor-pointer hover:bg-green-100 transition-colors ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
                        >
                          <Upload className="h-5 w-5 text-green-600 mr-2" />
                          <span className="text-sm font-medium text-green-700">Choose File</span>
                        </label>
                      </div>
                    </div>
                  </div>
                )}
                <span className="text-xs opacity-75 mt-1 block">
                  {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </span>
              </div>
            </div>
          </div>
        ))}
        
        {/* Loading indicator */}
        {isLoading && (
          <div className="flex justify-start">
            <div className="flex items-start space-x-2 max-w-xs lg:max-w-md">
              <div className="w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 bg-blue-500 text-white">
                <Bot className="h-4 w-4" />
              </div>
              <div className="px-4 py-2 rounded-lg bg-white text-gray-900 border border-gray-200">
                <div className="flex space-x-1">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Camera Modal */}
      {showCamera && (
        <div className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-4 max-w-md w-full mx-4">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-lg font-semibold">Take Photo</h3>
              <button
                onClick={stopCamera}
                className="p-2 hover:bg-gray-100 rounded-full"
              >
                <X className="h-5 w-5" />
              </button>
            </div>
            
            <div className="relative">
              <video
                id="camera-video"
                autoPlay
                playsInline
                className="w-full rounded-lg"
                style={{ maxHeight: '300px' }}
              />
            </div>
            
            <div className="flex justify-center mt-4">
              <button
                onClick={capturePhoto}
                disabled={isLoading}
                className="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-lg flex items-center space-x-2 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <Camera className="h-5 w-5" />
                <span>Capture Photo</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Voice Input Controls */}
      <div className="bg-white border-t p-4">
        {/* Recording Indicator */}
        {isRecording && (
          <div className="flex flex-col items-center mb-4">
            <div className="flex items-center space-x-2 mb-2">
              <div className="w-3 h-3 bg-red-500 rounded-full animate-pulse"></div>
              <span className="text-sm text-red-600 font-medium">Recording...</span>
            </div>
            <div className="flex items-center justify-center h-8">
              <SoundWaves isActive={isRecording} level={voiceLevel} />
            </div>
            {transcript && (
              <p className="text-sm text-gray-600 mt-2 text-center italic">"{transcript}"</p>
            )}
          </div>
        )}

        {/* Mic Error Display */}
        {micError && (
          <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg">
            <p className="text-sm text-red-600 text-center">{micError}</p>
          </div>
        )}

        <div className="flex justify-center">
          <div className="relative">
            {/* Outer pulsing ring when recording */}
            {isRecording && (
              <div className="absolute inset-0 rounded-full bg-green-400 animate-ping opacity-30"></div>
            )}
            {isRecording && (
              <div 
                className="absolute inset-0 rounded-full bg-green-400 opacity-20"
                style={{
                  transform: `scale(${1 + (voiceLevel / 300)})`,
                  transition: 'transform 0.1s ease-out'
                }}
              ></div>
            )}
            
            <button
              onClick={handleMicPress}
              disabled={isLoading || !sessionId}
              className={`relative w-16 h-16 rounded-full shadow-lg hover:shadow-xl transition-all duration-200 flex items-center justify-center ${
                isRecording 
                  ? 'bg-red-500 hover:bg-red-600 animate-pulse' 
                  : (!isLoading && sessionId ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-400 cursor-not-allowed')
              } text-white`}
              style={{
                transform: isRecording ? `scale(${1 + (voiceLevel / 500)})` : 'scale(1)',
                transition: 'transform 0.1s ease-out, background-color 0.2s'
              }}
            >
              {isRecording ? (
                <MicOff className="h-8 w-8" />
              ) : (
                <Mic className="h-8 w-8" />
              )}
            </button>
          </div>
        </div>
        
        <p className="text-center text-sm text-gray-600 mt-2">
          {isLoading ? 'Processing...' : 
           !sessionId ? 'Initializing...' :
           isRecording ? 'Tap to stop recording' : 'Tap to speak'}
        </p>
      </div>
    </div>
  );
};

export default VoiceInput;