import { create } from 'zustand';
import { persist } from 'zustand/middleware';

const useAppStore = create(
  persist(
    (set, get) => ({
      // User state
      user: null,
      isAuthenticated: false,
      
      // App state
      selectedLanguage: 'en',
      selectedCrops: [],
      farmingType: '',
      onboardingCompleted: false, // Always starts as false for each session
      currentScreen: 'splash',
      loading: true,
      error: null,
      sessionId: null,
      location: null,
      // UI state
      sidebarOpen: false,
      
      // Actions
      setUser: (user) => set({ user, isAuthenticated: true }),
      setLanguage: (language) => set({ selectedLanguage: language }),
      setCrops: (crops) => set({ selectedCrops: crops }),
      setFarmingType: (type) => set({ farmingType: type }),
      completeOnboarding: () => set({ onboardingCompleted: true }),
      setScreen: (screen) => set({ currentScreen: screen }),
      setLoading: (loading) => set({ loading }),
      setError: (error) => set({ error }),
      setSidebarOpen: (open) => set({ sidebarOpen: open }),
      setSessionId: (id) => set({ sessionId: id }),
      setLocation: (location) => set({ location }),
      // Initialize app
      initializeApp: async () => {
        set({ loading: true });
        
        // Simulate initialization delay
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // Mock user authentication
        const user = {
          uid: 'demo-user-' + Math.random().toString(36).substr(2, 9),
          isAnonymous: true
        };
        
        set({ 
          user, 
          isAuthenticated: true,
          loading: false,
          // Always start currentScreen as 'onboarding' after splash, as onboarding is not persisted
          currentScreen: 'onboarding'
        });
      },
      
      // Reset app state
      reset: () => set({
        user: null,
        isAuthenticated: false,
        selectedLanguage: 'English',
        selectedCrops: [],
        farmingType: '',
        onboardingCompleted: false,
        currentScreen: 'splash',
        loading: false,
        error: null,
        sidebarOpen: false,
        location: null,
      }),
    }),
    {
      name: 'farming-app-storage',
      partialize: (state) => ({
        selectedLanguage: state.selectedLanguage,
        selectedCrops: state.selectedCrops,
        farmingType: state.farmingType,
        // onboardingCompleted is explicitly not persisted
      }),
    }
  )
);

export default useAppStore;