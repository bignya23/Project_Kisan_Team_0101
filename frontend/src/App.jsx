import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import useAppStore from './store/appStore';

// Components
import SplashScreen from './components/SplashScreen';
import OnboardingFlow from './components/Onboarding/OnboardingFlow';

import Home from "./pages/Home.jsx"
import VoiceInput from './pages/Voicequery.jsx';

function App() {
  const { loading, onboardingCompleted, initializeApp } = useAppStore();

  useEffect(() => {
    initializeApp();
  }, [initializeApp]);

  // Show splash screen while loading
  if (loading) {
    return <SplashScreen />;
  }

  // Show onboarding if not completed, otherwise show Home
  if (!onboardingCompleted) {
    return <OnboardingFlow />;
  }

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/voice-input" element={<VoiceInput/>}/>
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;