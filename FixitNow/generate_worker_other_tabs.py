import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

write_file('app/(worker-tabs)/schedule.tsx', """
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
""")

write_file('app/(worker-tabs)/earnings.tsx', """
import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import Colors from '../../constants/Colors';
import { Ionicons } from '@expo/vector-icons';

export default function WorkerEarningsScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.headerTitle}>Earnings</Text>

      <ScrollView contentContainerStyle={styles.content}>
        
        <View style={styles.balanceCard}>
          <Text style={styles.balanceLabel}>Available for Payout</Text>
          <Text style={styles.balanceValue}>$420.50</Text>
          <TouchableOpacity style={styles.payoutBtn}>
            <Text style={styles.payoutBtnText}>Withdraw</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.statsRow}>
          <View style={styles.statCard}>
            <Text style={styles.statLabel}>This Week</Text>
            <Text style={styles.statValue}>$845.00</Text>
          </View>
          <View style={styles.statCard}>
            <Text style={styles.statLabel}>Jobs Done</Text>
            <Text style={styles.statValue}>12</Text>
          </View>
        </View>

        <Text style={styles.sectionTitle}>Recent Transactions</Text>
        
        {[
          { title: 'Circuit Breaker Replacement', date: 'Today, 2:30 PM', amount: '+$85.00', type: 'credit' },
          { title: 'Emergency Plumbing', date: 'Yesterday, 10:15 AM', amount: '+$120.00', type: 'credit' },
          { title: 'Bank Payout', date: 'Oct 22, 9:00 AM', amount: '-$500.00', type: 'debit' },
        ].map((tx, index) => (
          <View key={index} style={styles.txItem}>
            <View style={[styles.txIcon, { backgroundColor: tx.type === 'credit' ? '#D1FAE5' : '#FEE2E2' }]}>
              <Ionicons 
                name={tx.type === 'credit' ? 'arrow-down' : 'arrow-up'} 
                size={20} 
                color={tx.type === 'credit' ? Colors.success : Colors.error} 
              />
            </View>
            <View style={styles.txInfo}>
              <Text style={styles.txTitle}>{tx.title}</Text>
              <Text style={styles.txDate}>{tx.date}</Text>
            </View>
            <Text style={[styles.txAmount, { color: tx.type === 'credit' ? Colors.success : Colors.text }]}>
              {tx.amount}
            </Text>
          </View>
        ))}

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
  content: {
    padding: 20,
  },
  balanceCard: {
    backgroundColor: '#111827',
    borderRadius: 24,
    padding: 24,
    marginBottom: 20,
  },
  balanceLabel: {
    color: 'rgba(255,255,255,0.7)',
    fontSize: 14,
    fontWeight: '600',
    marginBottom: 8,
  },
  balanceValue: {
    color: Colors.white,
    fontSize: 40,
    fontWeight: '800',
    marginBottom: 20,
  },
  payoutBtn: {
    backgroundColor: Colors.secondary,
    paddingVertical: 12,
    borderRadius: 12,
    alignItems: 'center',
  },
  payoutBtnText: {
    color: Colors.text,
    fontWeight: '800',
    fontSize: 16,
  },
  statsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 32,
  },
  statCard: {
    width: '48%',
    backgroundColor: Colors.white,
    padding: 20,
    borderRadius: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    elevation: 2,
  },
  statLabel: {
    fontSize: 13,
    color: Colors.textSecondary,
    marginBottom: 8,
    fontWeight: '600',
  },
  statValue: {
    fontSize: 24,
    fontWeight: '800',
    color: Colors.text,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: Colors.text,
    marginBottom: 16,
  },
  txItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.white,
    padding: 16,
    borderRadius: 16,
    marginBottom: 12,
  },
  txIcon: {
    width: 40,
    height: 40,
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  txInfo: {
    flex: 1,
  },
  txTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 4,
  },
  txDate: {
    fontSize: 13,
    color: Colors.textSecondary,
  },
  txAmount: {
    fontSize: 16,
    fontWeight: '800',
  }
});
""")

write_file('app/(worker-tabs)/profile.tsx', """
import React from 'react';
import { View, Text, StyleSheet, ScrollView, Image, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import Colors from '../../constants/Colors';

export default function WorkerProfileScreen() {
  const router = useRouter();

  return (
    <View style={styles.container}>
      <Text style={styles.headerTitle}>Pro Profile</Text>

      <ScrollView contentContainerStyle={styles.content}>
        
        <View style={styles.profileCard}>
          <Image 
            source={{ uri: 'https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80' }} 
            style={styles.avatar} 
          />
          <View style={styles.profileInfo}>
            <View style={{ flexDirection: 'row', alignItems: 'center' }}>
              <Text style={styles.name}>Marcus Rivera</Text>
              <Ionicons name="checkmark-circle" size={18} color={Colors.primary} style={{ marginLeft: 4 }} />
            </View>
            <Text style={styles.role}>Master Electrician</Text>
            <Text style={styles.phone}>+1 (555) 987-6543</Text>
          </View>
        </View>

        <View style={styles.statsCard}>
          <View style={styles.statItem}>
            <Text style={styles.statValue}>4.9</Text>
            <Text style={styles.statLabel}>Rating</Text>
          </View>
          <View style={styles.statDivider} />
          <View style={styles.statItem}>
            <Text style={styles.statValue}>1.2k</Text>
            <Text style={styles.statLabel}>Jobs</Text>
          </View>
          <View style={styles.statDivider} />
          <View style={styles.statItem}>
            <Text style={styles.statValue}>3 Yrs</Text>
            <Text style={styles.statLabel}>Experience</Text>
          </View>
        </View>

        <View style={styles.menuContainer}>
          {[
            { icon: 'document-text', title: 'My Documents' },
            { icon: 'settings', title: 'Service Area Settings' },
            { icon: 'help-buoy', title: 'Pro Support' },
            { icon: 'log-out', title: 'Log Out', color: Colors.error, action: () => router.replace('/login') },
          ].map((item, index) => (
            <TouchableOpacity 
              key={index} 
              style={styles.menuItem}
              onPress={item.action}
            >
              <View style={[styles.menuIcon, item.color && { backgroundColor: '#FEF2F2' }]}>
                <Ionicons name={item.icon as any} size={20} color={item.color || Colors.text} />
              </View>
              <Text style={[styles.menuTitle, item.color && { color: item.color }]}>{item.title}</Text>
              <Ionicons name="chevron-forward" size={20} color={Colors.textSecondary} />
            </TouchableOpacity>
          ))}
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
  content: {
    padding: 20,
  },
  profileCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.white,
    padding: 20,
    borderRadius: 20,
    marginBottom: 16,
  },
  avatar: {
    width: 72,
    height: 72,
    borderRadius: 36,
    marginRight: 16,
  },
  profileInfo: {
    flex: 1,
  },
  name: {
    fontSize: 20,
    fontWeight: '800',
    color: Colors.text,
    marginBottom: 4,
  },
  role: {
    fontSize: 14,
    color: Colors.primary,
    fontWeight: '700',
    marginBottom: 4,
  },
  phone: {
    fontSize: 14,
    color: Colors.textSecondary,
  },
  statsCard: {
    flexDirection: 'row',
    backgroundColor: Colors.white,
    borderRadius: 20,
    padding: 20,
    marginBottom: 24,
  },
  statItem: {
    flex: 1,
    alignItems: 'center',
  },
  statValue: {
    fontSize: 20,
    fontWeight: '800',
    color: Colors.text,
    marginBottom: 4,
  },
  statLabel: {
    fontSize: 12,
    color: Colors.textSecondary,
    fontWeight: '600',
  },
  statDivider: {
    width: 1,
    backgroundColor: Colors.border,
    height: '100%',
  },
  menuContainer: {
    backgroundColor: Colors.white,
    borderRadius: 20,
    paddingHorizontal: 20,
  },
  menuItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 16,
    borderBottomWidth: 1,
    borderBottomColor: Colors.border,
  },
  menuIcon: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#F3F4F6',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  menuTitle: {
    flex: 1,
    fontSize: 16,
    fontWeight: '600',
    color: Colors.text,
  }
});
""")

print("Worker earnings and profile created")
