import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

write_file('app/(worker-tabs)/index.tsx', """
import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, Switch, TouchableOpacity, Image } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import Colors from '../../constants/Colors';

export default function WorkerHomeScreen() {
  const router = useRouter();
  const [isOnline, setIsOnline] = useState(true);

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <View style={styles.profileSection}>
          <Image 
            source={{ uri: 'https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80' }} 
            style={styles.avatar} 
          />
          <View>
            <Text style={styles.greeting}>Hi, Marcus</Text>
            <Text style={styles.role}>Master Electrician</Text>
          </View>
        </View>
        <View style={styles.onlineToggle}>
          <Text style={[styles.onlineText, { color: isOnline ? Colors.success : Colors.textSecondary }]}>
            {isOnline ? 'ONLINE' : 'OFFLINE'}
          </Text>
          <Switch 
            value={isOnline} 
            onValueChange={setIsOnline} 
            trackColor={{ false: Colors.border, true: '#D1FAE5' }}
            thumbColor={isOnline ? Colors.success : Colors.textSecondary}
          />
        </View>
      </View>

      <ScrollView style={styles.scrollContent} contentContainerStyle={{ paddingBottom: 40 }}>
        
        {/* Today's Summary */}
        <View style={styles.summaryContainer}>
          <View style={styles.summaryCard}>
            <Text style={styles.summaryValue}>3</Text>
            <Text style={styles.summaryLabel}>Jobs Today</Text>
          </View>
          <View style={styles.summaryCard}>
            <Text style={styles.summaryValue}>$245</Text>
            <Text style={styles.summaryLabel}>Earned</Text>
          </View>
          <View style={styles.summaryCard}>
            <View style={{ flexDirection: 'row', alignItems: 'center' }}>
              <Text style={styles.summaryValue}>4.9</Text>
              <Ionicons name="star" size={16} color={Colors.secondary} style={{ marginLeft: 4 }} />
            </View>
            <Text style={styles.summaryLabel}>Rating</Text>
          </View>
        </View>

        {/* New Requests Section */}
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>New Requests (1)</Text>
        </View>

        {isOnline ? (
          <TouchableOpacity 
            style={styles.requestCard} 
            activeOpacity={0.9} 
            onPress={() => router.push('/worker/job/1')}
          >
            <View style={styles.urgentBadge}>
              <Ionicons name="time" size={12} color={Colors.white} />
              <Text style={styles.urgentBadgeText}>URGENT</Text>
            </View>
            
            <View style={styles.requestHeader}>
              <Text style={styles.serviceName}>Circuit Breaker Replacement</Text>
              <Text style={styles.servicePrice}>Est. $85</Text>
            </View>
            
            <View style={styles.requestDetails}>
              <View style={styles.detailRow}>
                <Ionicons name="location" size={16} color={Colors.textSecondary} />
                <Text style={styles.detailText}>2.4 km • 242 Modernist Way, Apt 4B</Text>
              </View>
              <View style={styles.detailRow}>
                <Ionicons name="calendar" size={16} color={Colors.textSecondary} />
                <Text style={styles.detailText}>Today • As soon as possible</Text>
              </View>
            </View>
            
            <View style={styles.actionRow}>
              <TouchableOpacity style={styles.rejectBtn}>
                <Text style={styles.rejectBtnText}>Decline</Text>
              </TouchableOpacity>
              <TouchableOpacity style={styles.acceptBtn} onPress={() => router.push('/worker/job/1')}>
                <Text style={styles.acceptBtnText}>Review & Accept</Text>
              </TouchableOpacity>
            </View>
          </TouchableOpacity>
        ) : (
          <View style={styles.offlineState}>
            <Ionicons name="moon" size={48} color={Colors.textSecondary} />
            <Text style={styles.offlineTitle}>You are offline</Text>
            <Text style={styles.offlineDesc}>Go online to receive new job requests in your area.</Text>
          </View>
        )}

        {/* Upcoming Schedule */}
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Upcoming Schedule</Text>
          <TouchableOpacity>
            <Text style={styles.seeAllText}>See all</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.upcomingCard}>
          <View style={styles.upcomingHeader}>
            <View style={styles.timeBadge}>
              <Text style={styles.timeText}>3:00 PM</Text>
            </View>
            <View style={styles.statusBadge}>
              <Text style={styles.statusText}>CONFIRMED</Text>
            </View>
          </View>
          <Text style={styles.upcomingService}>Ceiling Fan Installation</Text>
          <Text style={styles.upcomingAddress}>1200 Tech Ave, Floor 3</Text>
        </View>

      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.background,
    paddingTop: 50,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingBottom: 16,
    borderBottomWidth: 1,
    borderBottomColor: Colors.border,
  },
  profileSection: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  avatar: {
    width: 48,
    height: 48,
    borderRadius: 24,
    marginRight: 12,
  },
  greeting: {
    fontSize: 20,
    fontWeight: '800',
    color: Colors.text,
  },
  role: {
    fontSize: 13,
    color: Colors.primary,
    fontWeight: '700',
  },
  onlineToggle: {
    alignItems: 'center',
  },
  onlineText: {
    fontSize: 10,
    fontWeight: '800',
    marginBottom: 4,
  },
  scrollContent: {
    padding: 20,
  },
  summaryContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 24,
  },
  summaryCard: {
    backgroundColor: Colors.white,
    padding: 16,
    borderRadius: 16,
    alignItems: 'center',
    width: '31%',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    elevation: 2,
  },
  summaryValue: {
    fontSize: 24,
    fontWeight: '800',
    color: Colors.text,
    marginBottom: 4,
  },
  summaryLabel: {
    fontSize: 12,
    color: Colors.textSecondary,
    fontWeight: '600',
  },
  sectionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
    marginTop: 8,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: Colors.text,
  },
  seeAllText: {
    color: Colors.primary,
    fontWeight: '600',
  },
  requestCard: {
    backgroundColor: Colors.white,
    borderRadius: 20,
    padding: 20,
    marginBottom: 24,
    borderWidth: 2,
    borderColor: Colors.urgent,
    shadowColor: Colors.urgent,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 12,
    elevation: 4,
  },
  urgentBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.urgent,
    paddingVertical: 4,
    paddingHorizontal: 8,
    borderRadius: 8,
    alignSelf: 'flex-start',
    marginBottom: 12,
  },
  urgentBadgeText: {
    color: Colors.white,
    fontSize: 10,
    fontWeight: '800',
    marginLeft: 4,
    letterSpacing: 0.5,
  },
  requestHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  serviceName: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.text,
    flex: 1,
  },
  servicePrice: {
    fontSize: 18,
    fontWeight: '800',
    color: Colors.success,
  },
  requestDetails: {
    marginBottom: 20,
  },
  detailRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 6,
  },
  detailText: {
    fontSize: 14,
    color: Colors.textSecondary,
    marginLeft: 8,
  },
  actionRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  rejectBtn: {
    flex: 1,
    paddingVertical: 14,
    borderRadius: 12,
    alignItems: 'center',
    marginRight: 12,
    backgroundColor: '#F3F4F6',
  },
  rejectBtnText: {
    color: Colors.textSecondary,
    fontWeight: '700',
    fontSize: 15,
  },
  acceptBtn: {
    flex: 2,
    paddingVertical: 14,
    borderRadius: 12,
    alignItems: 'center',
    backgroundColor: Colors.primary,
  },
  acceptBtnText: {
    color: Colors.white,
    fontWeight: '700',
    fontSize: 15,
  },
  offlineState: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: 40,
    backgroundColor: Colors.white,
    borderRadius: 20,
    marginBottom: 24,
  },
  offlineTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.text,
    marginTop: 16,
    marginBottom: 8,
  },
  offlineDesc: {
    fontSize: 14,
    color: Colors.textSecondary,
    textAlign: 'center',
  },
  upcomingCard: {
    backgroundColor: Colors.white,
    borderRadius: 16,
    padding: 16,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    elevation: 2,
  },
  upcomingHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  timeBadge: {
    backgroundColor: '#EFF6FF',
    paddingVertical: 4,
    paddingHorizontal: 8,
    borderRadius: 6,
  },
  timeText: {
    color: Colors.primary,
    fontWeight: '700',
    fontSize: 12,
  },
  statusBadge: {
    backgroundColor: '#D1FAE5',
    paddingVertical: 4,
    paddingHorizontal: 8,
    borderRadius: 6,
  },
  statusText: {
    color: Colors.success,
    fontWeight: '800',
    fontSize: 10,
  },
  upcomingService: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 4,
  },
  upcomingAddress: {
    fontSize: 13,
    color: Colors.textSecondary,
  }
});
""")

print("Worker home screen created")
