import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

write_file('app/booking/confirm.tsx', """
import React from 'react';
import { View, Text, StyleSheet, ScrollView, Image, TouchableOpacity, TextInput } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import Colors from '../../constants/Colors';
import Button from '../../components/Button';

export default function ConfirmBookingScreen() {
  const router = useRouter();

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={styles.urgentBadge}>
        <Text style={styles.urgentBadgeText}>URGENT REQUEST</Text>
      </View>
      
      <Text style={styles.title}>Confirm Your Booking</Text>
      <Text style={styles.subtitle}>Review your details before we dispatch our expert to your location.</Text>

      {/* Service Card */}
      <View style={styles.card}>
        <View style={styles.serviceHeader}>
          <Text style={styles.serviceTitle}>Emergency Plumbing</Text>
          <Text style={styles.servicePrice}>$85/hr</Text>
        </View>
        <View style={styles.etaContainer}>
          <Ionicons name="time" size={14} color={Colors.textSecondary} />
          <Text style={styles.etaText}>Est. arrival 45 mins</Text>
        </View>
        
        <View style={styles.technicianContainer}>
          <Image 
            source={{ uri: 'https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80' }} 
            style={styles.techAvatar} 
          />
          <View style={styles.techInfo}>
            <Text style={styles.techName}>Marcus Chen</Text>
            <View style={styles.ratingContainer}>
              <Ionicons name="star" size={14} color={Colors.warning} />
              <Text style={styles.ratingText}>4.9 (124 reviews)</Text>
            </View>
          </View>
          <View style={styles.verifiedBadge}>
            <Ionicons name="checkmark-circle" size={24} color={Colors.primary} />
          </View>
        </View>
      </View>

      {/* Details Card */}
      <View style={styles.card}>
        <View style={styles.detailRow}>
          <View style={styles.iconContainer}>
            <Ionicons name="location" size={20} color={Colors.primary} />
          </View>
          <View style={styles.detailInfo}>
            <Text style={styles.detailLabel}>SERVICE ADDRESS</Text>
            <Text style={styles.detailText}>242 Modernist Way, Apt 4B</Text>
            <Text style={styles.detailText}>Silicon Hills, CA 94021</Text>
          </View>
        </View>
        
        <View style={styles.divider} />
        
        <View style={styles.detailRow}>
          <View style={styles.iconContainer}>
            <Ionicons name="calendar" size={20} color={Colors.primary} />
          </View>
          <View style={styles.detailInfo}>
            <Text style={styles.detailLabel}>SCHEDULED TIME</Text>
            <Text style={styles.detailText}>Today, Oct 24 • 2:30 PM - 3:00 PM</Text>
          </View>
        </View>
      </View>

      {/* Payment Method Card */}
      <View style={styles.card}>
        <View style={styles.paymentHeader}>
          <Text style={styles.cardTitle}>Payment Method</Text>
          <TouchableOpacity>
            <Text style={styles.changeText}>CHANGE</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.paymentMethod}>
          <View style={styles.visaCard}>
            <Text style={styles.visaText}>VISA</Text>
          </View>
          <View style={styles.paymentInfo}>
            <Text style={styles.cardNumber}>•••• 4242</Text>
            <Text style={styles.cardExpiry}>EXPIRES 12/26</Text>
          </View>
          <Ionicons name="checkmark-circle" size={24} color={Colors.primary} />
        </View>
      </View>

      {/* Price Summary */}
      <View style={styles.priceSummaryCard}>
        <Text style={styles.cardTitle}>Price Summary</Text>
        
        <View style={styles.priceRow}>
          <Text style={styles.priceLabel}>Base Service Fee</Text>
          <Text style={styles.priceValue}>$45.00</Text>
        </View>
        <View style={styles.priceRow}>
          <Text style={styles.priceLabel}>Urgency Surcharge</Text>
          <Text style={[styles.priceValue, { color: Colors.error }]}>$20.00</Text>
        </View>
        <View style={styles.priceRow}>
          <Text style={styles.priceLabel}>Labor (Est. 1hr)</Text>
          <Text style={styles.priceValue}>$85.00</Text>
        </View>
        <View style={styles.priceRow}>
          <Text style={styles.priceLabel}>Estimated Tax</Text>
          <Text style={styles.priceValue}>$12.40</Text>
        </View>
        
        <View style={styles.totalRow}>
          <View>
            <Text style={styles.totalLabel}>TOTAL AMOUNT</Text>
            <Text style={styles.totalValue}>$162.40</Text>
          </View>
          <Text style={styles.finalBillText}>Final bill on completion</Text>
        </View>
        
        <View style={styles.promoContainer}>
          <TextInput 
            style={styles.promoInput} 
            placeholder="Promo code" 
            placeholderTextColor={Colors.textSecondary}
          />
          <TouchableOpacity style={styles.applyBtn}>
            <Text style={styles.applyBtnText}>APPLY</Text>
          </TouchableOpacity>
        </View>
        
        <Button 
          title="Confirm Booking" 
          onPress={() => router.push('/booking/tracking')} 
          style={{ marginTop: 24 }}
        />
        
        <Text style={styles.termsText}>
          By clicking confirm, you agree to our Terms of Service and authorize the hold of $162.40 on your payment method.
        </Text>
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
  urgentBadge: {
    backgroundColor: Colors.urgent,
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 16,
    alignSelf: 'flex-start',
    marginBottom: 16,
  },
  urgentBadgeText: {
    color: Colors.white,
    fontSize: 10,
    fontWeight: '800',
    letterSpacing: 0.5,
  },
  title: {
    fontSize: 28,
    fontWeight: '800',
    color: Colors.text,
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 15,
    color: Colors.textSecondary,
    marginBottom: 24,
    lineHeight: 22,
  },
  card: {
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
  serviceHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  serviceTitle: {
    fontSize: 20,
    fontWeight: '700',
    color: Colors.text,
  },
  servicePrice: {
    fontSize: 20,
    fontWeight: '700',
    color: Colors.primary,
  },
  etaContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },
  etaText: {
    fontSize: 13,
    color: Colors.textSecondary,
    marginLeft: 6,
  },
  technicianContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.background,
    padding: 12,
    borderRadius: 16,
  },
  techAvatar: {
    width: 48,
    height: 48,
    borderRadius: 24,
    marginRight: 12,
  },
  techInfo: {
    flex: 1,
  },
  techName: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 4,
  },
  ratingContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  ratingText: {
    fontSize: 13,
    color: Colors.textSecondary,
    marginLeft: 4,
    fontWeight: '500',
  },
  verifiedBadge: {
    marginLeft: 'auto',
  },
  detailRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
  },
  iconContainer: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#EFF6FF',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  detailInfo: {
    flex: 1,
  },
  detailLabel: {
    fontSize: 11,
    fontWeight: '700',
    color: Colors.textSecondary,
    marginBottom: 4,
    letterSpacing: 0.5,
  },
  detailText: {
    fontSize: 15,
    color: Colors.text,
    fontWeight: '500',
    marginBottom: 2,
  },
  divider: {
    height: 1,
    backgroundColor: Colors.border,
    marginVertical: 16,
    marginLeft: 56,
  },
  paymentHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.text,
  },
  changeText: {
    fontSize: 13,
    fontWeight: '700',
    color: Colors.primary,
  },
  paymentMethod: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.background,
    padding: 16,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: Colors.border,
  },
  visaCard: {
    backgroundColor: '#1A1F36',
    paddingHorizontal: 12,
    paddingVertical: 8,
    borderRadius: 6,
    marginRight: 16,
  },
  visaText: {
    color: Colors.white,
    fontWeight: '800',
    fontSize: 14,
    fontStyle: 'italic',
  },
  paymentInfo: {
    flex: 1,
  },
  cardNumber: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 2,
  },
  cardExpiry: {
    fontSize: 10,
    color: Colors.textSecondary,
    fontWeight: '600',
  },
  priceSummaryCard: {
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
  priceRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  priceLabel: {
    fontSize: 15,
    color: Colors.textSecondary,
  },
  priceValue: {
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
    marginBottom: 24,
  },
  totalLabel: {
    fontSize: 12,
    fontWeight: '700',
    color: Colors.primary,
    marginBottom: 4,
  },
  totalValue: {
    fontSize: 32,
    fontWeight: '800',
    color: Colors.text,
  },
  finalBillText: {
    fontSize: 11,
    color: Colors.textSecondary,
    fontStyle: 'italic',
    marginBottom: 6,
  },
  promoContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.white,
    borderWidth: 1,
    borderColor: Colors.border,
    borderRadius: 16,
    padding: 6,
    paddingLeft: 16,
  },
  promoInput: {
    flex: 1,
    fontSize: 15,
    color: Colors.text,
  },
  applyBtn: {
    backgroundColor: Colors.black,
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 12,
  },
  applyBtnText: {
    color: Colors.white,
    fontWeight: '700',
    fontSize: 13,
  },
  termsText: {
    fontSize: 11,
    color: Colors.textSecondary,
    textAlign: 'center',
    marginTop: 16,
    lineHeight: 16,
  },
});
""")

print("Confirm booking screen created")
