import React from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity, SafeAreaView, Dimensions } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import Colors from '../../constants/Colors';
import Button from '../../components/Button';

const { width } = Dimensions.get('window');

export default function TrackingScreen() {
  const router = useRouter();

  return (
    <View style={styles.container}>
      {/* Map Background (Simulated) */}
      <View style={styles.mapContainer}>
        <Image 
          source={{ uri: 'https://images.unsplash.com/photo-1524661135-423995f22d0b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80' }} 
          style={styles.mapImage} 
          blurRadius={1}
        />
        <View style={styles.mapOverlay} />
        
        {/* ETA Marker */}
        <View style={styles.etaMarker}>
          <View style={styles.etaDot} />
          <Text style={styles.etaMarkerText}>Arriving in 12 mins</Text>
        </View>
      </View>

      {/* Bottom Sheet */}
      <View style={styles.bottomSheet}>
        <View style={styles.dragHandle} />
        
        <View style={styles.techCard}>
          <View style={styles.avatarContainer}>
            <Image 
              source={{ uri: 'https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80' }} 
              style={styles.techAvatar} 
            />
            <View style={styles.proBadge}>
              <Text style={styles.proBadgeText}>PRO</Text>
            </View>
          </View>
          
          <View style={styles.techInfo}>
            <Text style={styles.techName}>Marcus Rivera</Text>
            <View style={styles.ratingRow}>
              <Ionicons name="star" size={14} color={Colors.warning} />
              <Text style={styles.ratingText}>4.9</Text>
              <Text style={styles.jobsText}>(1.2k jobs)</Text>
            </View>
            <Text style={styles.techType}>MASTER ELECTRICIAN</Text>
          </View>
        </View>
        
        <View style={styles.actionButtons}>
          <TouchableOpacity style={styles.actionBtn}>
            <Ionicons name="chatbubble" size={20} color={Colors.primary} />
            <Text style={styles.actionBtnText}>Chat</Text>
          </TouchableOpacity>
          <TouchableOpacity style={[styles.actionBtn, { backgroundColor: Colors.primary }]} onPress={() => router.push('/booking/in-service')}>
            <Ionicons name="call" size={20} color={Colors.white} />
            <Text style={[styles.actionBtnText, { color: Colors.white }]}>Call</Text>
          </TouchableOpacity>
        </View>
        
        {/* Progress Card */}
        <View style={styles.progressCard}>
          <View style={styles.progressHeader}>
            <Text style={styles.progressTitle}>Service Progress</Text>
            <Text style={styles.progressEta}>ETA 2:45 PM</Text>
          </View>
          
          <View style={styles.timeline}>
            <View style={styles.timelineLine} />
            <View style={styles.timelineActiveLine} />
            
            <View style={styles.timelineStep}>
              <View style={[styles.timelineIcon, styles.timelineIconActive]}>
                <Ionicons name="checkmark" size={16} color={Colors.white} />
              </View>
              <Text style={styles.timelineTextActive}>CONFIRMED</Text>
            </View>
            
            <View style={styles.timelineStep}>
              <View style={[styles.timelineIcon, styles.timelineIconActive]}>
                <Ionicons name="flash" size={16} color={Colors.white} />
              </View>
              <Text style={styles.timelineTextActive}>HEADING OVER</Text>
            </View>
            
            <View style={styles.timelineStep}>
              <View style={styles.timelineIcon}>
                <Ionicons name="construct" size={16} color={Colors.textSecondary} />
              </View>
              <Text style={styles.timelineText}>WORKING</Text>
            </View>
            
            <View style={styles.timelineStep}>
              <View style={styles.timelineIcon}>
                <Ionicons name="checkmark-done" size={16} color={Colors.textSecondary} />
              </View>
              <Text style={styles.timelineText}>DONE</Text>
            </View>
          </View>
        </View>
        
        {/* Service Details */}
        <View style={styles.serviceDetailsCard}>
          <View style={styles.urgentBadge}>
            <Text style={styles.urgentBadgeText}>URGENT FIX</Text>
          </View>
          <Text style={styles.serviceName}>Circuit Breaker Replacement</Text>
          <Text style={styles.serviceDuration}>Est. Duration: 45-60 mins</Text>
          
          <TouchableOpacity style={styles.viewDetailsBtn}>
            <Text style={styles.viewDetailsText}>View Details</Text>
            <Ionicons name="chevron-forward" size={16} color={Colors.primary} />
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.background,
  },
  mapContainer: {
    flex: 1,
    position: 'relative',
  },
  mapImage: {
    width: '100%',
    height: '100%',
    opacity: 0.8,
  },
  mapOverlay: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: 'rgba(239, 246, 255, 0.4)',
  },
  etaMarker: {
    position: 'absolute',
    top: '30%',
    left: '20%',
    backgroundColor: Colors.white,
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 30,
    flexDirection: 'row',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 12,
    elevation: 4,
  },
  etaDot: {
    width: 10,
    height: 10,
    borderRadius: 5,
    backgroundColor: Colors.primary,
    marginRight: 10,
  },
  etaMarkerText: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
  },
  bottomSheet: {
    backgroundColor: Colors.white,
    borderTopLeftRadius: 32,
    borderTopRightRadius: 32,
    padding: 24,
    paddingTop: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: -8 },
    shadowOpacity: 0.05,
    shadowRadius: 20,
    elevation: 10,
    height: '75%',
  },
  dragHandle: {
    width: 48,
    height: 4,
    backgroundColor: Colors.border,
    borderRadius: 2,
    alignSelf: 'center',
    marginBottom: 24,
  },
  techCard: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 24,
  },
  avatarContainer: {
    position: 'relative',
    marginRight: 16,
  },
  techAvatar: {
    width: 72,
    height: 72,
    borderRadius: 36,
    borderWidth: 2,
    borderColor: Colors.border,
  },
  proBadge: {
    position: 'absolute',
    bottom: -4,
    right: -4,
    backgroundColor: Colors.secondary,
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 8,
    borderWidth: 2,
    borderColor: Colors.white,
  },
  proBadgeText: {
    color: Colors.text,
    fontSize: 9,
    fontWeight: '800',
  },
  techInfo: {
    flex: 1,
  },
  techName: {
    fontSize: 24,
    fontWeight: '800',
    color: Colors.text,
    marginBottom: 4,
  },
  ratingRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 6,
  },
  ratingText: {
    fontSize: 15,
    fontWeight: '700',
    color: Colors.text,
    marginLeft: 6,
  },
  jobsText: {
    fontSize: 14,
    color: Colors.textSecondary,
    marginLeft: 6,
  },
  techType: {
    fontSize: 11,
    fontWeight: '800',
    color: Colors.primary,
    letterSpacing: 1,
  },
  actionButtons: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 24,
  },
  actionBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#F1F5F9',
    paddingVertical: 16,
    borderRadius: 16,
    marginHorizontal: 6,
  },
  actionBtnText: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
    marginLeft: 8,
  },
  progressCard: {
    backgroundColor: Colors.white,
    borderRadius: 24,
    padding: 24,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: Colors.border,
  },
  progressHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 24,
  },
  progressTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.text,
  },
  progressEta: {
    fontSize: 13,
    fontWeight: '700',
    color: Colors.textSecondary,
  },
  timeline: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    position: 'relative',
  },
  timelineLine: {
    position: 'absolute',
    top: 16,
    left: 20,
    right: 20,
    height: 2,
    backgroundColor: Colors.border,
    zIndex: 0,
  },
  timelineActiveLine: {
    position: 'absolute',
    top: 16,
    left: 20,
    width: '40%',
    height: 2,
    backgroundColor: Colors.primary,
    zIndex: 1,
  },
  timelineStep: {
    alignItems: 'center',
    width: width / 5,
    zIndex: 2,
  },
  timelineIcon: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: Colors.white,
    borderWidth: 2,
    borderColor: Colors.border,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 8,
  },
  timelineIconActive: {
    backgroundColor: Colors.primary,
    borderColor: Colors.primary,
  },
  timelineText: {
    fontSize: 9,
    fontWeight: '700',
    color: Colors.textSecondary,
    textAlign: 'center',
  },
  timelineTextActive: {
    fontSize: 9,
    fontWeight: '800',
    color: Colors.text,
    textAlign: 'center',
  },
  serviceDetailsCard: {
    backgroundColor: '#F8FAFC',
    borderRadius: 24,
    padding: 20,
  },
  urgentBadge: {
    backgroundColor: '#FFEDD5',
    paddingVertical: 4,
    paddingHorizontal: 8,
    borderRadius: 8,
    alignSelf: 'flex-start',
    marginBottom: 12,
  },
  urgentBadgeText: {
    color: '#C2410C',
    fontSize: 10,
    fontWeight: '800',
  },
  serviceName: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.text,
    marginBottom: 4,
  },
  serviceDuration: {
    fontSize: 13,
    color: Colors.textSecondary,
    marginBottom: 12,
  },
  viewDetailsBtn: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  viewDetailsText: {
    fontSize: 14,
    fontWeight: '700',
    color: Colors.primary,
    marginRight: 4,
  },
});
