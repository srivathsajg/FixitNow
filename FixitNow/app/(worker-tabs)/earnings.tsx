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
