import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { MessageCircle, Mic } from 'lucide-react';
import useAppStore from '../store/appStore';
import { getTranslation } from '../utils/translations';


const Home = () => {
  const { selectedLanguage, user } = useAppStore();
  const navigate = useNavigate();
  const [queryPreference, setQueryPreference] = useState(null);

  // Check if user has a preference and redirect accordingly
  useEffect(() => {
    if (queryPreference) {
      const targetRoute = queryPreference === 'text' ? '/text-query' : '/voice-input';
      navigate(targetRoute);
    }
  }, [queryPreference, navigate,setQueryPreference]);

  const onTextQueryPress = () => {
    setQueryPreference('text');
  };

  const onVoiceQueryPress = () => {
    setQueryPreference('voice');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-blue-50 flex items-center justify-center p-4">
      <div className="max-w-2xl w-full text-center">
        {/* Welcome Section */}
        <div className="mb-12">
          <div className="w-24 h-24 bg-white rounded-full flex items-center justify-center mx-auto mb-6 shadow-lg">
            <span className="text-5xl">🌾</span>
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            Welcome back, Farmer! 👋
          </h1>
          <p className="text-lg text-gray-600 mb-2">
            How can I help you today?
          </p>
          <p className="text-sm text-gray-500">
            {getTranslation(selectedLanguage, 'userId')}: {user?.uid?.substring(0, 8) || 'Anonymous'}
          </p>
        </div>

        {/* Query Options */}
        <div className="mb-8">
          <h2 className="text-2xl font-semibold text-gray-800 mb-8">
            Solve your problem by:
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-lg mx-auto">
            {/* Text Query */}
            <button
              onClick={onTextQueryPress}
              className="group bg-white rounded-2xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2 border-2 border-transparent hover:border-blue-200 w-full"
            >
              <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:bg-blue-200 transition-colors">
                <MessageCircle className="h-8 w-8 text-blue-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">
                Text Query
              </h3>
              <p className="text-gray-600 text-sm">
                Type your farming questions and get instant answers
              </p>
            </button>

            {/* Voice Query */}
            <button
              onClick={onVoiceQueryPress}
              className="group bg-white rounded-2xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2 border-2 border-transparent hover:border-green-200 w-full"
            >
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:bg-green-200 transition-colors">
                <Mic className="h-8 w-8 text-green-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">
                Voice Query
              </h3>
              <p className="text-gray-600 text-sm">
                Speak your questions naturally and get voice responses
              </p>
            </button>
          </div>
        </div>

        {/* Quick tip */}
        <div className="bg-white/50 backdrop-blur-sm rounded-xl p-6 border border-white/20">
          <p className="text-gray-700 text-sm">
            💡 <strong>Tip:</strong> Ask about crop diseases, weather conditions, market prices, farming techniques, or any agricultural concerns you have.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Home;