import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

write_file('app/worker/job/[id].tsx', """
import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, SafeAreaView } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import Colors from '../../../constants/Colors';
import Button from '../../../components/Button';

export default function WorkerJobScreen() {
  const { id } = useLocalSearchParams();
  const router = useRouter();
  
  // Simulated state machine for the job
  // States: 'new', 'accepted', 'on_way', 'arrived', 'in_progress', 'completed'
  const [jobState, setJobState] = useState('new');
  const [otp, setOtp] = useState('');

  const handleNextAction = () => {
    switch (jobState) {
      case 'new': setJobState('accepted'); break;
      case 'accepted': setJobState('on_way'); break;
      case 'on_way': setJobState('arrived'); break;
      case 'arrived': setJobState('in_progress'); break;
      case 'in_progress': setJobState('completed'); break;
      case 'completed': router.replace('/(worker-tabs)'); break;
    }
  };

  const getActionText = () => {
    switch (jobState) {
      case 'new': return 'Accept Request';
      case 'accepted': return 'Start Journey';
      case 'on_way': return 'Mark as Arrived';
      case 'arrived': return 'Verify OTP & Start Job';
      case 'in_progress': return 'Complete Job';
      case 'completed': return 'Back to Home';
      default: return 'Next';
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} style={styles.backBtn}>
          <Ionicons name="arrow-back" size={24} color={Colors.text} />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Job Details</Text>
        <View style={{ width: 40 }} />
      </View>

      <ScrollView style={styles.scrollContent} contentContainerStyle={{ paddingBottom: 100 }}>
        
        <View style={styles.urgentBadge}>
          <Text style={styles.urgentBadgeText}>URGENT REQUEST</Text>
        </View>
        
        <View style={styles.mainInfo}>
          <Text style={styles.serviceName}>Circuit Breaker Replacement</Text>
          <Text style={styles.price}>Est. $85.00</Text>
        </View>

        {/* Client Details Card */}
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Client Details</Text>
          
          <View style={styles.clientRow}>
            <View style={styles.clientAvatar}>
              <Ionicons name="person" size={24} color={Colors.white} />
            </View>
            <View style={styles.clientInfo}>
              <Text style={styles.clientName}>Sri K.</Text>
              <Text style={styles.clientRating}>4.8 ★ (12 bookings)</Text>
            </View>
            
            {jobState !== 'new' && (
              <View style={styles.actionBtns}>
                <TouchableOpacity style={styles.iconBtn}>
                  <Ionicons name="chatbubble" size={20} color={Colors.primary} />
                </TouchableOpacity>
                <TouchableOpacity style={styles.iconBtn}>
                  <Ionicons name="call" size={20} color={Colors.primary} />
                </TouchableOpacity>
              </View>
            )}
          </View>
        </View>

        {/* Location Card */}
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Location</Text>
          <View style={styles.locationRow}>
            <Ionicons name="location" size={24} color={Colors.primary} />
            <View style={styles.locationInfo}>
              <Text style={styles.address}>242 Modernist Way, Apt 4B</Text>
              <Text style={styles.distance}>2.4 km away (Est. 12 mins)</Text>
            </View>
          </View>
          
          {jobState === 'accepted' || jobState === 'on_way' ? (
            <TouchableOpacity style={styles.mapBtn}>
              <Text style={styles.mapBtnText}>Open in Maps</Text>
              <Ionicons name="navigate" size={16} color={Colors.primary} style={{ marginLeft: 8 }} />
            </TouchableOpacity>
          ) : null}
        </View>

        {/* Job Timeline / Status */}
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Job Status</Text>
          
          <View style={styles.timeline}>
            <View style={styles.timelineItem}>
              <View style={[styles.dot, jobState !== 'new' && styles.dotActive]} />
              <Text style={[styles.timelineText, jobState !== 'new' && styles.timelineTextActive]}>Accepted</Text>
            </View>
            <View style={styles.timelineItem}>
              <View style={[styles.dot, (jobState === 'arrived' || jobState === 'in_progress' || jobState === 'completed') && styles.dotActive]} />
              <Text style={[styles.timelineText, (jobState === 'arrived' || jobState === 'in_progress' || jobState === 'completed') && styles.timelineTextActive]}>Arrived</Text>
            </View>
            <View style={styles.timelineItem}>
              <View style={[styles.dot, (jobState === 'in_progress' || jobState === 'completed') && styles.dotActive]} />
              <Text style={[styles.timelineText, (jobState === 'in_progress' || jobState === 'completed') && styles.timelineTextActive]}>In Progress</Text>
            </View>
            <View style={styles.timelineItem}>
              <View style={[styles.dot, jobState === 'completed' && styles.dotActive]} />
              <Text style={[styles.timelineText, jobState === 'completed' && styles.timelineTextActive]}>Completed</Text>
            </View>
          </View>
        </View>

        {/* OTP Input for Arrived State */}
        {jobState === 'arrived' && (
          <View style={styles.otpCard}>
            <Text style={styles.otpTitle}>Client OTP</Text>
            <Text style={styles.otpDesc}>Ask the client for the 4-digit code to start the job.</Text>
            <View style={styles.otpBox}>
              <Text style={styles.otpDigit}>5 2 8 4</Text>
            </View>
          </View>
        )}

      </ScrollView>

      {/* Floating Action Button */}
      <View style={styles.footer}>
        {jobState === 'new' && (
          <TouchableOpacity style={styles.declineBtn}>
            <Text style={styles.declineText}>Decline</Text>
          </TouchableOpacity>
        )}
        <Button 
          title={getActionText()} 
          onPress={handleNextAction} 
          style={{ flex: 1, backgroundColor: jobState === 'completed' ? Colors.success : Colors.primary }} 
        />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
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
    borderBottomWidth: 1,
    borderBottomColor: Colors.border,
  },
  backBtn: {
    padding: 8,
    marginLeft: -8,
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.text,
  },
  scrollContent: {
    padding: 20,
  },
  urgentBadge: {
    backgroundColor: Colors.urgent,
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 8,
    alignSelf: 'flex-start',
    marginBottom: 16,
  },
  urgentBadgeText: {
    color: Colors.white,
    fontSize: 10,
    fontWeight: '800',
    letterSpacing: 0.5,
  },
  mainInfo: {
    marginBottom: 24,
  },
  serviceName: {
    fontSize: 28,
    fontWeight: '800',
    color: Colors.text,
    marginBottom: 8,
  },
  price: {
    fontSize: 24,
    fontWeight: '800',
    color: Colors.success,
  },
  card: {
    backgroundColor: Colors.white,
    borderRadius: 20,
    padding: 20,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    elevation: 2,
  },
  cardTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 16,
  },
  clientRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  clientAvatar: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: Colors.textSecondary,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  clientInfo: {
    flex: 1,
  },
  clientName: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 4,
  },
  clientRating: {
    fontSize: 14,
    color: Colors.textSecondary,
  },
  actionBtns: {
    flexDirection: 'row',
  },
  iconBtn: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#EFF6FF',
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: 12,
  },
  locationRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
  },
  locationInfo: {
    marginLeft: 16,
    flex: 1,
  },
  address: {
    fontSize: 16,
    fontWeight: '600',
    color: Colors.text,
    marginBottom: 4,
  },
  distance: {
    fontSize: 14,
    color: Colors.textSecondary,
  },
  mapBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 16,
    paddingTop: 16,
    borderTopWidth: 1,
    borderTopColor: Colors.border,
  },
  mapBtnText: {
    fontSize: 14,
    fontWeight: '700',
    color: Colors.primary,
  },
  timeline: {
    paddingLeft: 8,
  },
  timelineItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  dot: {
    width: 16,
    height: 16,
    borderRadius: 8,
    backgroundColor: Colors.border,
    marginRight: 16,
  },
  dotActive: {
    backgroundColor: Colors.primary,
  },
  timelineText: {
    fontSize: 15,
    color: Colors.textSecondary,
    fontWeight: '500',
  },
  timelineTextActive: {
    color: Colors.text,
    fontWeight: '700',
  },
  otpCard: {
    backgroundColor: '#EFF6FF',
    borderRadius: 20,
    padding: 20,
    alignItems: 'center',
    marginBottom: 16,
  },
  otpTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.primary,
    marginBottom: 8,
  },
  otpDesc: {
    fontSize: 14,
    color: Colors.textSecondary,
    textAlign: 'center',
    marginBottom: 16,
  },
  otpBox: {
    backgroundColor: Colors.white,
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: Colors.primary,
  },
  otpDigit: {
    fontSize: 24,
    fontWeight: '800',
    color: Colors.text,
    letterSpacing: 8,
  },
  footer: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    backgroundColor: Colors.white,
    padding: 20,
    paddingBottom: 32,
    borderTopWidth: 1,
    borderTopColor: Colors.border,
    flexDirection: 'row',
  },
  declineBtn: {
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 24,
    marginRight: 16,
    backgroundColor: '#F3F4F6',
    borderRadius: 12,
  },
  declineText: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.textSecondary,
  }
});
""")

print("Worker job detail screen created")
