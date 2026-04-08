import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, SafeAreaView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import Colors from '../constants/Colors';
import Button from '../components/Button';

export default function SupportScreen() {
  const router = useRouter();

  return (
    <SafeAreaView style={styles.safeArea}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} style={styles.backBtn}>
          <Ionicons name="arrow-back" size={24} color={Colors.text} />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>FixitNow</Text>
        <View style={styles.headerRight}>
          <Ionicons name="person-circle" size={32} color={Colors.text} />
        </View>
      </View>
      
      <ScrollView style={styles.container} contentContainerStyle={styles.content}>
        <Text style={styles.title}>
          How can we <Text style={{ color: Colors.primary }}>help you</Text> today?
        </Text>
        <Text style={styles.subtitle}>
          Find answers to your questions about home repairs, bookings, and payments, or connect with our support squad.
        </Text>

        {/* Support Options */}
        <View style={styles.card}>
          <View style={styles.iconContainer}>
            <Ionicons name="chatbubble" size={24} color={Colors.white} />
          </View>
          <Text style={styles.cardTitle}>Live Chat</Text>
          <View style={styles.statusRow}>
            <Text style={styles.statusText}>Wait time: </Text>
            <Text style={styles.statusHighlight}>Under 2 mins</Text>
          </View>
          <Button title="START CHAT" onPress={() => {}} style={{ marginTop: 16 }} />
        </View>

        <View style={styles.card}>
          <View style={[styles.iconContainer, { backgroundColor: Colors.urgent }]}>
            <Ionicons name="call" size={24} color={Colors.white} />
          </View>
          <Text style={styles.cardTitle}>Call Support</Text>
          <View style={styles.statusRow}>
            <Text style={styles.statusText}>Available 24/7 for </Text>
            <Text style={[styles.statusHighlight, { color: Colors.urgent, fontSize: 10, fontWeight: '800' }]}>EMERGENCIES</Text>
          </View>
          <Button 
            title="CALL NOW" 
            onPress={() => {}} 
            variant="secondary" 
            style={{ marginTop: 16, backgroundColor: Colors.border }} 
            textStyle={{ color: Colors.text }} 
          />
        </View>

        <View style={styles.card}>
          <View style={[styles.iconContainer, { backgroundColor: Colors.warning }]}>
            <Ionicons name="mail" size={24} color={Colors.text} />
          </View>
          <Text style={styles.cardTitle}>Email Us</Text>
          <View style={styles.statusRow}>
            <Text style={styles.statusText}>Average response in </Text>
            <Text style={[styles.statusHighlight, { color: Colors.text }]}>4 hours</Text>
          </View>
          <Button 
            title="SEND TICKET" 
            onPress={() => {}} 
            variant="secondary" 
            style={{ marginTop: 16, backgroundColor: Colors.border }} 
            textStyle={{ color: Colors.text }} 
          />
        </View>

        {/* FAQ Section */}
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Frequently Asked</Text>
          <TouchableOpacity>
            <Text style={styles.seeAllText}>VIEW ALL TOPICS</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.faqList}>
          {[
            { title: 'Payments & Refunds', icon: 'cash' },
            { title: 'Service Guarantees', icon: 'shield-checkmark' },
            { title: 'Managing Bookings', icon: 'calendar' },
            { title: 'Pro Requirements', icon: 'people' },
          ].map((item, index) => (
            <TouchableOpacity key={index} style={styles.faqItem}>
              <View style={styles.faqIcon}>
                <Ionicons name={item.icon as any} size={20} color={Colors.primary} />
              </View>
              <Text style={styles.faqTitle}>{item.title}</Text>
              <Ionicons name="chevron-forward" size={20} color={Colors.textSecondary} />
            </TouchableOpacity>
          ))}
        </View>

        {/* Safety Guarantee */}
        <View style={styles.safetyCard}>
          <View style={styles.safetyBadge}>
            <Text style={styles.safetyBadgeText}>OUR PROMISE</Text>
          </View>
          <Text style={styles.safetyTitle}>FixitNow Safety Guarantee</Text>
          <Text style={styles.safetyDesc}>
            Every professional is background-checked and vetted. If anything goes wrong during a job, we're here to make it right with $1M coverage.
          </Text>
          <TouchableOpacity style={styles.safetyBtn}>
            <Text style={styles.safetyBtnText}>Learn about Safety</Text>
          </TouchableOpacity>
        </View>
        <View style={{ height: 40 }} />
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: Colors.background,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    paddingVertical: 16,
    backgroundColor: Colors.white,
  },
  backBtn: {
    padding: 4,
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: Colors.text,
  },
  headerRight: {
    width: 32,
    height: 32,
    borderRadius: 16,
    overflow: 'hidden',
  },
  container: {
    flex: 1,
  },
  content: {
    padding: 24,
  },
  title: {
    fontSize: 32,
    fontWeight: '800',
    color: Colors.text,
    lineHeight: 40,
    marginBottom: 16,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: Colors.textSecondary,
    lineHeight: 24,
    textAlign: 'center',
    marginBottom: 32,
    paddingHorizontal: 16,
  },
  card: {
    backgroundColor: Colors.white,
    borderRadius: 24,
    padding: 24,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.03,
    shadowRadius: 12,
    elevation: 2,
  },
  iconContainer: {
    width: 48,
    height: 48,
    borderRadius: 16,
    backgroundColor: Colors.primary,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 16,
  },
  cardTitle: {
    fontSize: 22,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 8,
  },
  statusRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  statusText: {
    fontSize: 14,
    color: Colors.textSecondary,
  },
  statusHighlight: {
    fontSize: 14,
    fontWeight: '700',
    color: Colors.primary,
  },
  sectionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-end',
    marginTop: 16,
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '700',
    color: Colors.text,
    maxWidth: '60%',
    lineHeight: 30,
  },
  seeAllText: {
    color: Colors.primary,
    fontWeight: '700',
    fontSize: 12,
    letterSpacing: 0.5,
  },
  faqList: {
    marginBottom: 32,
  },
  faqItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.white,
    padding: 20,
    borderRadius: 20,
    marginBottom: 12,
  },
  faqIcon: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#EFF6FF',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  faqTitle: {
    flex: 1,
    fontSize: 16,
    fontWeight: '600',
    color: Colors.text,
  },
  safetyCard: {
    backgroundColor: '#0F172A',
    borderRadius: 24,
    padding: 24,
    marginBottom: 20,
  },
  safetyBadge: {
    backgroundColor: Colors.primary,
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 16,
    alignSelf: 'flex-start',
    marginBottom: 20,
  },
  safetyBadgeText: {
    color: Colors.white,
    fontSize: 10,
    fontWeight: '800',
    letterSpacing: 0.5,
  },
  safetyTitle: {
    fontSize: 28,
    fontWeight: '800',
    color: Colors.white,
    lineHeight: 34,
    marginBottom: 16,
  },
  safetyDesc: {
    fontSize: 15,
    color: '#94A3B8',
    lineHeight: 24,
    marginBottom: 24,
  },
  safetyBtn: {
    backgroundColor: Colors.white,
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 24,
    alignSelf: 'flex-start',
  },
  safetyBtnText: {
    color: '#0F172A',
    fontWeight: '700',
    fontSize: 14,
  },
});
