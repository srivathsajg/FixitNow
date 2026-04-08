import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, TouchableOpacity } from 'react-native';
import { useRouter } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import Colors from '../constants/Colors';
import Button from '../components/Button';

export default function LocationScreen() {
  const router = useRouter();

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <View style={styles.iconContainer}>
          <Ionicons name="location" size={64} color={Colors.primary} />
        </View>
        
        <Text style={styles.title}>What's your location?</Text>
        <Text style={styles.subtitle}>We need your location to show available services and experts nearby.</Text>
        
        <Button 
          title="Allow Location Access" 
          onPress={() => router.replace('/(tabs)')} 
          style={{ width: '100%', marginBottom: 16 }}
        />
        
        <TouchableOpacity style={styles.manualBtn} onPress={() => router.replace('/(tabs)')}>
          <Text style={styles.manualBtnText}>Enter location manually</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.white,
  },
  content: {
    flex: 1,
    padding: 24,
    justifyContent: 'center',
    alignItems: 'center',
  },
  iconContainer: {
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: '#EFF6FF',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 40,
  },
  title: {
    fontSize: 28,
    fontWeight: '800',
    color: Colors.text,
    textAlign: 'center',
    marginBottom: 16,
  },
  subtitle: {
    fontSize: 16,
    color: Colors.textSecondary,
    textAlign: 'center',
    marginBottom: 48,
    lineHeight: 24,
    paddingHorizontal: 20,
  },
  manualBtn: {
    padding: 16,
  },
  manualBtnText: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.primary,
  },
});
