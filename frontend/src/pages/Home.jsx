import React, { useState } from 'react';
import { Calendar, Mic, Send } from 'lucide-react';

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

  const demoResponses = [
    "Hello! I'm here to help you with your farming questions. How can I assist you today?",
    "That's a great question about crop management. Based on current agricultural practices, I recommend...",
    "For pest control, you should consider integrated pest management techniques. Here are some suggestions...",
    "Weather conditions are crucial for farming. Let me provide you with some insights about your query...",
    "Regarding soil health, it's important to maintain proper pH levels and nutrient balance..."
  ];

  const handleSendMessage = () => {
    if (inputText.trim()) {
      const newMessage = {
        id: Date.now(),
        text: inputText,
        isUser: true,
        timestamp: new Date()
      };

      const botResponse = {
        id: Date.now() + 1,
        text: demoResponses[Math.floor(Math.random() * demoResponses.length)],
        isUser: false,
        timestamp: new Date()
      };

      setMessages(prev => [...prev, newMessage, botResponse]);
      setInputText('');
      setHasStartedChat(true);
    }
  };

  const handleVoiceInput = () => {
    setIsListening(true);
    
    // Simulate voice input
    setTimeout(() => {
      const voiceText = "How do I protect my crops from pests?";
      setInputText(voiceText);
      setIsListening(false);
      
      // Auto-send after voice input simulation
      setTimeout(() => {
        const newMessage = {
          id: Date.now(),
          text: voiceText,
          isUser: true,
          timestamp: new Date()
        };

        const botResponse = {
          id: Date.now() + 1,
          text: "For pest protection, I recommend using integrated pest management (IPM) techniques. This includes regular monitoring, using beneficial insects, applying organic pesticides when necessary, and maintaining crop rotation. Would you like specific recommendations for your crop type?",
          isUser: false,
          timestamp: new Date()
        };

        setMessages(prev => [...prev, newMessage, botResponse]);
        setInputText('');
        setHasStartedChat(true);
      }, 500);
    }, 2000);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

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

          {/* Mic Button */}
          <button
            onClick={handleVoiceInput}
            disabled={isListening}
            className={`w-20 h-20 rounded-full flex items-center justify-center mb-12 shadow-lg transition-all duration-200 transform hover:scale-105 active:scale-95 ${
              isListening 
                ? 'bg-red-500 animate-pulse shadow-red-200' 
                : 'bg-green-500 hover:bg-green-600 shadow-green-200'
            }`}
          >
            <Mic className="h-8 w-8 text-white" />
          </button>

          {isListening && (
            <p className="text-gray-600 mb-8 animate-pulse text-center">
              {getTranslation(selectedLanguage, 'listening')}
            </p>
          )}
        </main>

        {/* Bottom Input */}
        <div className="p-5 border-t border-gray-100">
          <div className="flex items-end bg-gray-50 rounded-3xl px-4 py-3 shadow-sm">
            <textarea
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder={getTranslation(selectedLanguage, 'enterText')}
              className="flex-1 bg-transparent outline-none text-gray-800 placeholder-gray-500 resize-none max-h-32 py-2"
              rows="1"
            />
            <button
              onClick={handleSendMessage}
              disabled={!inputText.trim()}
              className={`ml-3 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
                inputText.trim()
                  ? 'bg-green-500 hover:bg-green-600 text-white shadow-md'
                  : 'bg-gray-300 text-gray-500 cursor-not-allowed'
              }`}
            >
              <Send className="h-5 w-5" />
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Chat Interface
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
              <p className="text-sm leading-6">{message.text}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Input Container */}
      <div className="p-5 border-t border-gray-100">
        <div className="flex items-end bg-gray-50 rounded-3xl px-4 py-3 shadow-sm">
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your message..."
            className="flex-1 bg-transparent outline-none text-gray-800 placeholder-gray-500 resize-none max-h-32 py-2"
            rows="1"
          />
          <button
            onClick={handleSendMessage}
            disabled={!inputText.trim()}
            className={`ml-3 p-2 rounded-full transition-all duration-200 transform hover:scale-105 active:scale-95 ${
              inputText.trim()
                ? 'bg-green-500 hover:bg-green-600 text-white shadow-md'
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
          >
            <Send className="h-5 w-5" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default Home;