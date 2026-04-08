import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

write_file('app/(tabs)/index.tsx', """
import React from 'react';
import { View, Text, StyleSheet, ScrollView, Image, TouchableOpacity, TextInput } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import Colors from '../../constants/Colors';
import { categories, user } from '../../data/mock';

export default function HomeScreen() {
  const router = useRouter();

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <View style={styles.locationContainer}>
          <View style={styles.pinIconContainer}>
            <Ionicons name="location" size={20} color={Colors.primary} />
          </View>
          <View style={styles.locationTextContainer}>
            <Text style={styles.locationLabel}>YOUR LOCATION</Text>
            <View style={{ flexDirection: 'row', alignItems: 'center' }}>
              <Text style={styles.locationText}>{user.location}</Text>
              <Ionicons name="chevron-down" size={16} color={Colors.text} style={{ marginLeft: 4 }} />
            </View>
          </View>
        </View>
        <Image source={{ uri: user.avatar }} style={styles.avatar} />
      </View>

      <ScrollView showsVerticalScrollIndicator={false} contentContainerStyle={styles.scrollContent}>
        {/* Greeting */}
        <View style={styles.greetingContainer}>
          <Text style={styles.greetingTitle}>Hi {user.name} 👋</Text>
          <Text style={styles.greetingSubtitle}>What can we help you with today?</Text>
        </View>

        {/* Search Bar */}
        <View style={styles.searchContainer}>
          <Ionicons name="search" size={20} color={Colors.textSecondary} />
          <TextInput 
            style={styles.searchInput} 
            placeholder="Search for 'AC Repair', 'Plumber'..."
            placeholderTextColor={Colors.textSecondary}
          />
        </View>

        {/* Active Booking */}
        <TouchableOpacity 
          style={styles.activeBookingCard} 
          onPress={() => router.push('/booking/tracking')}
          activeOpacity={0.9}
        >
          <View style={styles.activeBookingIcon}>
            <Ionicons name="flash" size={24} color={Colors.primary} />
          </View>
          <View style={styles.activeBookingInfo}>
            <Text style={styles.activeBookingTitle}>Electrician is arriving</Text>
            <Text style={styles.activeBookingDesc}>Scheduled for 10:30 AM • In 12 mins</Text>
          </View>
          <TouchableOpacity style={styles.trackBtn} onPress={() => router.push('/booking/tracking')}>
            <Text style={styles.trackBtnText}>Track</Text>
          </TouchableOpacity>
        </TouchableOpacity>

        {/* Hero Banner */}
        <TouchableOpacity style={styles.heroBanner} activeOpacity={0.9} onPress={() => router.push('/booking/confirm')}>
          <View style={styles.heroContent}>
            <View style={styles.urgentBadge}>
              <Ionicons name="time" size={12} color={Colors.white} />
              <Text style={styles.urgentBadgeText}>URGENT HELP</Text>
            </View>
            <Text style={styles.heroTitle}>Emergency repair at your doorstep in 15-30 mins</Text>
            <TouchableOpacity style={styles.bookNowBtn}>
              <Text style={styles.bookNowText}>Book Now</Text>
            </TouchableOpacity>
          </View>
          <View style={styles.heroDiscountBadge}>
            <Text style={styles.heroDiscountText}>Flat $10 Off</Text>
          </View>
        </TouchableOpacity>

        {/* Popular Services */}
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Popular Services</Text>
          <TouchableOpacity>
            <Text style={styles.seeAllText}>See all</Text>
          </TouchableOpacity>
        </View>
        
        <View style={styles.servicesGrid}>
          {categories.map((category) => (
            <TouchableOpacity key={category.id} style={styles.categoryItem} activeOpacity={0.7}>
              <View style={styles.categoryIconContainer}>
                <Ionicons name={category.icon as any} size={28} color={Colors.primary} />
              </View>
              <Text style={styles.categoryName} numberOfLines={2} textAlign="center">{category.name.toUpperCase()}</Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Emergency Services */}
        <View style={styles.emergencyContainer}>
          <View style={styles.emergencyHeader}>
            <Ionicons name="warning" size={20} color={Colors.urgent} />
            <Text style={styles.emergencyTitle}>Emergency Services</Text>
          </View>
          
          <TouchableOpacity style={styles.emergencyCard} activeOpacity={0.8} onPress={() => router.push('/booking/confirm')}>
            <View style={styles.emergencyCardIconContainer}>
              <Ionicons name="home" size={24} color={Colors.white} />
            </View>
            <View style={styles.emergencyCardInfo}>
              <View style={{ flexDirection: 'row', alignItems: 'center', marginBottom: 4 }}>
                <Text style={styles.emergencyCardTitle}>Burst Pipe Repair</Text>
                <View style={styles.priorityBadge}>
                  <Text style={styles.priorityText}>PRIORITY</Text>
                </View>
              </View>
              <Text style={styles.emergencyCardDesc}>Technician matches in <Text style={{ color: Colors.urgent, fontWeight: '700' }}>2 mins</Text></Text>
            </View>
            <Ionicons name="chevron-forward" size={20} color={Colors.textSecondary} />
          </TouchableOpacity>
          
          <TouchableOpacity style={[styles.emergencyCard, { marginTop: 12 }]} activeOpacity={0.8}>
            <View style={[styles.emergencyCardIconContainer, { backgroundColor: '#F1F5F9' }]}>
              <Ionicons name="lock-closed" size={24} color="#475569" />
            </View>
            <View style={styles.emergencyCardInfo}>
              <Text style={styles.emergencyCardTitle}>Locksmith Service</Text>
              <Text style={styles.emergencyCardDesc}>24/7 Availability</Text>
            </View>
            <Ionicons name="chevron-forward" size={20} color={Colors.textSecondary} />
          </TouchableOpacity>
        </View>
        
        {/* Ongoing Offers */}
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Ongoing Offers</Text>
        </View>
        <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.offersScroll}>
          <View style={[styles.offerCard, { backgroundColor: '#FFE4E6' }]}>
            <Text style={[styles.offerTitle, { color: '#9F1239' }]}>Summer AC Refresh</Text>
            <Text style={[styles.offerSubtitle, { color: '#E11D48' }]}>30% OFF</Text>
            <View style={{ marginTop: 'auto', flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-end' }}>
              <TouchableOpacity style={styles.offerBtn}>
                <Text style={styles.offerBtnText}>Book Now</Text>
              </TouchableOpacity>
            </View>
          </View>
          
          <View>
            <View style={[styles.smallOfferCard, { backgroundColor: '#DBEAFE', marginBottom: 12 }]}>
              <Text style={[styles.offerTitleSmall, { color: '#1E3A8A' }]}>Full Home Deep Clean</Text>
              <Text style={[styles.offerSubtitleSmall, { color: '#2563EB' }]}>From $49</Text>
            </View>
            <View style={[styles.smallOfferCard, { backgroundColor: '#D1FAE5' }]}>
              <Text style={[styles.offerTitleSmall, { color: '#065F46' }]}>Verified Pros Only</Text>
              <Text style={[styles.offerSubtitleSmall, { color: '#059669' }]}>Background Checked</Text>
            </View>
          </View>
        </ScrollView>
        <View style={{ height: 40 }} />
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.white,
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
  locationContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  pinIconContainer: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: '#EFF6FF',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  locationTextContainer: {
    justifyContent: 'center',
  },
  locationLabel: {
    fontSize: 10,
    fontWeight: '700',
    color: Colors.textSecondary,
    marginBottom: 2,
    letterSpacing: 0.5,
  },
  locationText: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
  },
  avatar: {
    width: 40,
    height: 40,
    borderRadius: 20,
  },
  scrollContent: {
    padding: 20,
  },
  greetingContainer: {
    marginTop: 10,
    marginBottom: 20,
  },
  greetingTitle: {
    fontSize: 28,
    fontWeight: '800',
    color: Colors.text,
    marginBottom: 4,
  },
  greetingSubtitle: {
    fontSize: 16,
    color: Colors.textSecondary,
  },
  searchContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.background,
    borderRadius: 16,
    paddingHorizontal: 16,
    paddingVertical: 14,
    marginBottom: 24,
  },
  searchInput: {
    flex: 1,
    marginLeft: 12,
    fontSize: 16,
    color: Colors.text,
  },
  activeBookingCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.white,
    borderRadius: 20,
    padding: 16,
    marginBottom: 24,
    borderWidth: 2,
    borderColor: Colors.primary,
    shadowColor: Colors.primary,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 12,
    elevation: 4,
  },
  activeBookingIcon: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#EFF6FF',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  activeBookingInfo: {
    flex: 1,
  },
  activeBookingTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 4,
  },
  activeBookingDesc: {
    fontSize: 13,
    color: Colors.textSecondary,
  },
  trackBtn: {
    backgroundColor: '#EFF6FF',
    paddingVertical: 8,
    paddingHorizontal: 16,
    borderRadius: 8,
  },
  trackBtnText: {
    color: Colors.primary,
    fontWeight: '700',
    fontSize: 14,
  },
  heroBanner: {
    backgroundColor: Colors.primary,
    borderRadius: 24,
    padding: 24,
    marginBottom: 32,
    overflow: 'hidden',
    position: 'relative',
  },
  heroContent: {
    width: '70%',
  },
  urgentBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(255,255,255,0.2)',
    paddingVertical: 4,
    paddingHorizontal: 8,
    borderRadius: 8,
    alignSelf: 'flex-start',
    marginBottom: 12,
  },
  urgentBadgeText: {
    color: Colors.white,
    fontSize: 10,
    fontWeight: '700',
    marginLeft: 4,
    letterSpacing: 0.5,
  },
  heroTitle: {
    fontSize: 22,
    fontWeight: '800',
    color: Colors.white,
    lineHeight: 30,
    marginBottom: 16,
  },
  bookNowBtn: {
    backgroundColor: Colors.secondary,
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 24,
    alignSelf: 'flex-start',
  },
  bookNowText: {
    color: Colors.text,
    fontWeight: '700',
    fontSize: 14,
  },
  heroDiscountBadge: {
    position: 'absolute',
    bottom: 20,
    right: 20,
    backgroundColor: 'rgba(255,255,255,0.2)',
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 16,
  },
  heroDiscountText: {
    color: Colors.white,
    fontWeight: '700',
    fontSize: 12,
  },
  sectionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '700',
    color: Colors.text,
  },
  seeAllText: {
    color: Colors.primary,
    fontWeight: '600',
    fontSize: 14,
  },
  servicesGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 24,
  },
  categoryItem: {
    width: '23%',
    alignItems: 'center',
    marginBottom: 20,
  },
  categoryIconContainer: {
    width: 64,
    height: 64,
    borderRadius: 32,
    backgroundColor: Colors.white,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    elevation: 2,
    borderWidth: 1,
    borderColor: '#F1F5F9',
  },
  categoryName: {
    fontSize: 10,
    fontWeight: '700',
    color: Colors.text,
  },
  emergencyContainer: {
    backgroundColor: '#F5E6E1',
    borderRadius: 24,
    padding: 20,
    marginBottom: 32,
  },
  emergencyHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  emergencyTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.urgent,
    marginLeft: 8,
  },
  emergencyCard: {
    backgroundColor: Colors.white,
    borderRadius: 16,
    padding: 16,
    flexDirection: 'row',
    alignItems: 'center',
  },
  emergencyCardIconContainer: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#C2410C',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  emergencyCardInfo: {
    flex: 1,
  },
  emergencyCardTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
  },
  priorityBadge: {
    backgroundColor: '#C2410C',
    paddingVertical: 2,
    paddingHorizontal: 6,
    borderRadius: 4,
    marginLeft: 8,
  },
  priorityText: {
    color: Colors.white,
    fontSize: 9,
    fontWeight: '800',
  },
  emergencyCardDesc: {
    fontSize: 13,
    color: Colors.textSecondary,
    marginTop: 2,
  },
  offersScroll: {
    paddingRight: 20,
  },
  offerCard: {
    width: 180,
    height: 220,
    borderRadius: 24,
    padding: 20,
    marginRight: 16,
  },
  offerTitle: {
    fontSize: 20,
    fontWeight: '800',
    lineHeight: 24,
    marginBottom: 8,
  },
  offerSubtitle: {
    fontSize: 14,
    fontWeight: '700',
  },
  offerBtn: {
    backgroundColor: '#7F1D1D',
    paddingVertical: 8,
    paddingHorizontal: 16,
    borderRadius: 16,
  },
  offerBtnText: {
    color: Colors.white,
    fontWeight: '700',
    fontSize: 12,
  },
  smallOfferCard: {
    width: 220,
    height: 104,
    borderRadius: 20,
    padding: 16,
    justifyContent: 'center',
  },
  offerTitleSmall: {
    fontSize: 16,
    fontWeight: '700',
    marginBottom: 4,
  },
  offerSubtitleSmall: {
    fontSize: 12,
    fontWeight: '600',
  },
});
""")

print("Home screen created")
