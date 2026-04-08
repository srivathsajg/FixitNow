import { Stack } from 'expo-router';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import Colors from '../constants/Colors';

export default function RootLayout() {
  return (
    <SafeAreaProvider>
      <Stack
        screenOptions={{
          headerShown: false,
          contentStyle: { backgroundColor: Colors.background }
        }}
      >
        <Stack.Screen name="index" />
        <Stack.Screen name="(tabs)" />
        <Stack.Screen name="booking/confirm" options={{ headerShown: true, title: 'FixitNow', headerBackTitle: 'Back' }} />
        <Stack.Screen name="booking/in-service" options={{ headerShown: true, title: 'FixitNow', headerBackTitle: 'Back' }} />
        <Stack.Screen name="booking/tracking" options={{ headerShown: true, title: 'FixitNow', headerBackTitle: 'Back' }} />
      </Stack>
    </SafeAreaProvider>
  );
}
