import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import Colors from '../../constants/Colors';
import { Ionicons } from '@expo/vector-icons';

export default function WorkerScheduleScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.headerTitle}>Schedule</Text>
      
      <View style={styles.tabsContainer}>
        <TouchableOpacity style={[styles.tab, styles.activeTab]}>
          <Text style={[styles.tabText, styles.activeTabText]}>Upcoming</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.tab}>
          <Text style={styles.tabText}>Past Jobs</Text>
        </TouchableOpacity>
      </View>

      <ScrollView contentContainerStyle={styles.content}>
        <Text style={styles.dateLabel}>TODAY, OCT 24</Text>
        
        <View style={styles.jobCard}>
          <View style={styles.jobHeader}>
            <View style={styles.timeBadge}>
              <Text style={styles.timeText}>3:00 PM - 4:00 PM</Text>
            </View>
            <View style={styles.statusBadge}>
              <Text style={styles.statusText}>CONFIRMED</Text>
            </View>
          </View>
          
          <Text style={styles.jobTitle}>Ceiling Fan Installation</Text>
          <Text style={styles.jobAddress}>1200 Tech Ave, Floor 3</Text>
          
          <View style={styles.jobFooter}>
            <Text style={styles.clientName}>Client: Sarah J.</Text>
            <Text style={styles.jobPrice}>Est. $65.00</Text>
          </View>
        </View>

        <Text style={styles.dateLabel}>TOMORROW, OCT 25</Text>
        
        <View style={styles.jobCard}>
          <View style={styles.jobHeader}>
            <View style={[styles.timeBadge, { backgroundColor: '#F3F4F6' }]}>
              <Text style={[styles.timeText, { color: Colors.textSecondary }]}>10:00 AM - 11:30 AM</Text>
            </View>
          </View>
          
          <Text style={styles.jobTitle}>Complete House Wiring Check</Text>
          <Text style={styles.jobAddress}>45 West End Drive</Text>
          
          <View style={styles.jobFooter}>
            <Text style={styles.clientName}>Client: Michael B.</Text>
            <Text style={styles.jobPrice}>Est. $120.00</Text>
          </View>
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
  headerTitle: {
    fontSize: 28,
    fontWeight: '800',
    color: Colors.text,
    paddingHorizontal: 20,
    marginBottom: 16,
  },
  tabsContainer: {
    flexDirection: 'row',
    paddingHorizontal: 20,
    marginBottom: 20,
  },
  tab: {
    paddingVertical: 8,
    paddingHorizontal: 16,
    marginRight: 12,
    borderRadius: 20,
    backgroundColor: Colors.white,
    borderWidth: 1,
    borderColor: Colors.border,
  },
  activeTab: {
    backgroundColor: Colors.text,
    borderColor: Colors.text,
  },
  tabText: {
    fontSize: 14,
    fontWeight: '600',
    color: Colors.textSecondary,
  },
  activeTabText: {
    color: Colors.white,
  },
  content: {
    padding: 20,
  },
  dateLabel: {
    fontSize: 12,
    fontWeight: '800',
    color: Colors.textSecondary,
    marginBottom: 12,
    letterSpacing: 1,
  },
  jobCard: {
    backgroundColor: Colors.white,
    borderRadius: 16,
    padding: 16,
    marginBottom: 24,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    elevation: 2,
  },
  jobHeader: {
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
  jobTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 4,
  },
  jobAddress: {
    fontSize: 14,
    color: Colors.textSecondary,
    marginBottom: 16,
  },
  jobFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingTop: 16,
    borderTopWidth: 1,
    borderTopColor: Colors.border,
  },
  clientName: {
    fontSize: 14,
    fontWeight: '600',
    color: Colors.text,
  },
  jobPrice: {
    fontSize: 16,
    fontWeight: '800',
    color: Colors.success,
  }
});
