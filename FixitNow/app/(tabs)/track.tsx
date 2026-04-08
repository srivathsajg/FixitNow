import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import Colors from '../../constants/Colors';
import Button from '../../components/Button';
import { useRouter } from 'expo-router';

export default function TrackTabScreen() {
  const router = useRouter();
  
  return (
    <View style={styles.container}>
      <View style={styles.iconContainer}>
        <Text style={{ fontSize: 64 }}>🗺️</Text>
      </View>
      <Text style={styles.title}>Active Services</Text>
      <Text style={styles.subtitle}>You have an ongoing service for Electrician. Track its real-time progress here.</Text>
      <Button 
        title="View Live Tracking" 
        onPress={() => router.push('/booking/tracking')} 
        style={{ marginTop: 24, width: '100%' }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.white,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 32,
  },
  iconContainer: {
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: '#EFF6FF',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 24,
  },
  title: {
    fontSize: 24,
    fontWeight: '800',
    color: Colors.text,
    marginBottom: 12,
  },
  subtitle: {
    fontSize: 16,
    color: Colors.textSecondary,
    textAlign: 'center',
    lineHeight: 24,
  },
});
