import React from 'react';
import { View, Text, StyleSheet, ScrollView, Image, TouchableOpacity, TextInput } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import Colors from '../../constants/Colors';
import Button from '../../components/Button';

export default function InServiceScreen() {
  const router = useRouter();

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      {/* Technician Card */}
      <View style={styles.techCard}>
        <View style={styles.avatarContainer}>
          <Image 
            source={{ uri: 'https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80' }} 
            style={styles.techAvatar} 
          />
          <View style={styles.proBadge}>
            <Ionicons name="checkmark-circle" size={16} color={Colors.white} />
          </View>
        </View>
        
        <View style={styles.techInfo}>
          <View style={styles.nameRow}>
            <Text style={styles.techName}>Marcus Chen</Text>
            <View style={styles.arrivedBadge}>
              <Text style={styles.arrivedText}>ARRIVED</Text>
            </View>
          </View>
          <Text style={styles.techDetails}>Expert Plumber • 4.9 ★ (240+ jobs)</Text>
          
          <View style={styles.actionBtns}>
            <TouchableOpacity style={styles.iconBtn}>
              <Ionicons name="call" size={20} color={Colors.primary} />
            </TouchableOpacity>
            <TouchableOpacity style={styles.iconBtn}>
              <Ionicons name="chatbubble" size={20} color={Colors.primary} />
            </TouchableOpacity>
          </View>
        </View>
      </View>

      {/* OTP Card */}
      <View style={styles.otpCard}>
        <Text style={styles.otpTitle}>VERIFY OTP TO START WORK</Text>
        <Text style={styles.otpDesc}>Ask Marcus for the 4-digit code displayed on his device to authorize the session.</Text>
        
        <View style={styles.otpInputContainer}>
          <View style={[styles.otpBox, styles.otpBoxFilled]}>
            <Text style={styles.otpDigit}>5</Text>
          </View>
          <View style={styles.otpBox}>
            <Text style={styles.otpDigit}>-</Text>
          </View>
          <View style={styles.otpBox}>
            <Text style={styles.otpDigit}>-</Text>
          </View>
          <View style={styles.otpBox}>
            <Text style={styles.otpDigit}>-</Text>
          </View>
        </View>
        
        <Button title="Verify & Start Work" onPress={() => {}} />
      </View>

      {/* Work in Progress Card */}
      <View style={styles.card}>
        <View style={styles.cardHeader}>
          <Text style={styles.cardTitle}>Work in Progress</Text>
          <Text style={styles.etaText}>Est. 45 mins left</Text>
        </View>
        
        <View style={styles.progressBarBg}>
          <View style={styles.progressBarFill} />
        </View>
        
        <View style={styles.statusList}>
          <View style={styles.statusItem}>
            <Ionicons name="checkmark-circle" size={24} color={Colors.primary} />
            <View style={styles.statusInfo}>
              <Text style={styles.statusTitle}>Technician Arrived</Text>
              <Text style={styles.statusTime}>Completed at 10:45 AM</Text>
            </View>
          </View>
          
          <View style={styles.statusItem}>
            <Ionicons name="radio-button-on" size={24} color={Colors.primary} />
            <View style={styles.statusInfo}>
              <Text style={styles.statusTitle}>Initial Diagnostics</Text>
              <Text style={[styles.statusTime, { color: Colors.primary }]}>Ongoing...</Text>
            </View>
          </View>
          
          <View style={styles.statusItem}>
            <Ionicons name="ellipse" size={24} color={Colors.border} />
            <View style={styles.statusInfo}>
              <Text style={[styles.statusTitle, { color: Colors.textSecondary }]}>Repair Execution</Text>
              <Text style={styles.statusTime}>Waiting</Text>
            </View>
          </View>
        </View>
      </View>

      {/* Before Photos */}
      <View style={styles.card}>
        <View style={styles.cardHeader}>
          <Text style={styles.cardTitle}>Before Photos</Text>
          <TouchableOpacity>
            <Text style={styles.addText}>Add New</Text>
          </TouchableOpacity>
        </View>
        
        <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.photosScroll}>
          <Image 
            source={{ uri: 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80' }} 
            style={styles.photo} 
          />
          <Image 
            source={{ uri: 'https://images.unsplash.com/photo-1581094288338-2314dddb7ece?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80' }} 
            style={styles.photo} 
          />
          <TouchableOpacity style={styles.addPhotoBtn}>
            <Ionicons name="camera" size={24} color={Colors.textSecondary} />
            <Text style={styles.addPhotoText}>UPLOAD</Text>
          </TouchableOpacity>
        </ScrollView>
      </View>

      {/* Estimated Cost */}
      <View style={styles.card}>
        <View style={styles.cardHeader}>
          <View style={{ flexDirection: 'row', alignItems: 'center' }}>
            <Ionicons name="receipt" size={20} color={Colors.text} style={{ marginRight: 8 }} />
            <Text style={styles.cardTitle}>Estimated Cost</Text>
          </View>
        </View>
        
        <View style={styles.costRow}>
          <Text style={styles.costLabel}>Service Visit Base</Text>
          <Text style={styles.costValue}>$49.00</Text>
        </View>
        <View style={styles.costRow}>
          <Text style={styles.costLabel}>Estimated Labor (1hr)</Text>
          <Text style={styles.costValue}>$85.00</Text>
        </View>
        <View style={styles.costRow}>
          <Text style={styles.costLabel}>Emergency Surcharge</Text>
          <Text style={[styles.costValue, { color: Colors.urgent }]}>+$25.00</Text>
        </View>
        
        <View style={styles.totalRow}>
          <View>
            <Text style={styles.runningTotalLabel}>RUNNING TOTAL</Text>
            <Text style={styles.totalValue}>$159.00</Text>
          </View>
          <TouchableOpacity style={styles.detailsBtn}>
            <Text style={styles.detailsBtnText}>Details</Text>
          </TouchableOpacity>
        </View>
      </View>
      <View style={{ height: 40 }} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.background,
  },
  content: {
    padding: 20,
  },
  techCard: {
    flexDirection: 'row',
    backgroundColor: Colors.white,
    borderRadius: 24,
    padding: 20,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.03,
    shadowRadius: 12,
    elevation: 2,
  },
  avatarContainer: {
    position: 'relative',
    marginRight: 16,
  },
  techAvatar: {
    width: 80,
    height: 80,
    borderRadius: 24,
  },
  proBadge: {
    position: 'absolute',
    bottom: -6,
    right: -6,
    backgroundColor: Colors.secondary,
    padding: 4,
    borderRadius: 12,
    borderWidth: 2,
    borderColor: Colors.white,
  },
  techInfo: {
    flex: 1,
  },
  nameRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 4,
  },
  techName: {
    fontSize: 20,
    fontWeight: '800',
    color: Colors.text,
  },
  arrivedBadge: {
    backgroundColor: Colors.urgent,
    paddingVertical: 4,
    paddingHorizontal: 8,
    borderRadius: 8,
    marginLeft: 8,
  },
  arrivedText: {
    color: Colors.white,
    fontSize: 9,
    fontWeight: '800',
  },
  techDetails: {
    fontSize: 13,
    color: Colors.textSecondary,
    marginBottom: 12,
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
    marginRight: 12,
  },
  otpCard: {
    backgroundColor: '#EFF6FF',
    borderRadius: 24,
    padding: 24,
    marginBottom: 16,
  },
  otpTitle: {
    fontSize: 12,
    fontWeight: '800',
    color: Colors.primary,
    textAlign: 'center',
    marginBottom: 8,
    letterSpacing: 0.5,
  },
  otpDesc: {
    fontSize: 14,
    color: Colors.textSecondary,
    textAlign: 'center',
    marginBottom: 20,
    lineHeight: 20,
  },
  otpInputContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    marginBottom: 24,
  },
  otpBox: {
    width: 60,
    height: 72,
    backgroundColor: Colors.white,
    borderRadius: 16,
    justifyContent: 'center',
    alignItems: 'center',
    marginHorizontal: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    elevation: 2,
  },
  otpBoxFilled: {
    borderWidth: 2,
    borderColor: Colors.primary,
  },
  otpDigit: {
    fontSize: 28,
    fontWeight: '800',
    color: Colors.text,
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
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 20,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.text,
  },
  etaText: {
    fontSize: 13,
    fontWeight: '700',
    color: Colors.primary,
  },
  progressBarBg: {
    height: 8,
    backgroundColor: Colors.border,
    borderRadius: 4,
    marginBottom: 24,
  },
  progressBarFill: {
    width: '30%',
    height: '100%',
    backgroundColor: Colors.primary,
    borderRadius: 4,
  },
  statusList: {},
  statusItem: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 20,
  },
  statusInfo: {
    marginLeft: 16,
    flex: 1,
  },
  statusTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 4,
  },
  statusTime: {
    fontSize: 13,
    color: Colors.textSecondary,
  },
  addText: {
    fontSize: 14,
    fontWeight: '700',
    color: Colors.primary,
  },
  photosScroll: {
    paddingRight: 8,
  },
  photo: {
    width: 100,
    height: 100,
    borderRadius: 16,
    marginRight: 12,
  },
  addPhotoBtn: {
    width: 100,
    height: 100,
    borderRadius: 16,
    borderWidth: 2,
    borderColor: Colors.border,
    borderStyle: 'dashed',
    justifyContent: 'center',
    alignItems: 'center',
  },
  addPhotoText: {
    fontSize: 10,
    fontWeight: '700',
    color: Colors.textSecondary,
    marginTop: 8,
  },
  costRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  costLabel: {
    fontSize: 15,
    color: Colors.textSecondary,
  },
  costValue: {
    fontSize: 15,
    fontWeight: '600',
    color: Colors.text,
  },
  totalRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-end',
    marginTop: 16,
    paddingTop: 16,
    borderTopWidth: 1,
    borderTopColor: Colors.border,
  },
  runningTotalLabel: {
    fontSize: 10,
    fontWeight: '800',
    color: Colors.textSecondary,
    letterSpacing: 0.5,
    marginBottom: 4,
  },
  totalValue: {
    fontSize: 28,
    fontWeight: '800',
    color: Colors.text,
  },
  detailsBtn: {
    backgroundColor: '#EFF6FF',
    paddingVertical: 8,
    paddingHorizontal: 16,
    borderRadius: 16,
    marginBottom: 4,
  },
  detailsBtnText: {
    fontSize: 13,
    fontWeight: '700',
    color: Colors.primary,
  },
});
