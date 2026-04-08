import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

write_file('constants/Colors.ts', """
export default {
  primary: '#1F51E5',
  primaryLight: '#3D6FF6',
  primaryDark: '#0D33A6',
  secondary: '#FFB800',
  secondaryLight: '#FFE399',
  background: '#F8F9FA',
  card: '#FFFFFF',
  text: '#111827',
  textSecondary: '#6B7280',
  border: '#E5E7EB',
  error: '#EF4444',
  success: '#10B981',
  warning: '#F59E0B',
  info: '#3B82F6',
  urgent: '#C2410C', // for urgent banners
  urgentBg: '#FFEDD5',
  black: '#000000',
  white: '#FFFFFF',
};
""")

write_file('types/index.ts', """
export interface ServiceCategory {
  id: string;
  name: string;
  icon: string;
  color?: string;
}

export interface Service {
  id: string;
  categoryId: string;
  name: string;
  description: string;
  price: number;
  estimatedTime: string;
  isEmergency?: boolean;
}

export interface Technician {
  id: string;
  name: string;
  rating: number;
  jobsCompleted: number;
  distance: string;
  eta: string;
  pricePerHour: number;
  avatar: string;
  isVerified: boolean;
  type: string; // e.g. "Master Electrician"
}

export interface Booking {
  id: string;
  serviceId: string;
  technicianId: string;
  status: 'pending' | 'confirmed' | 'on_the_way' | 'arrived' | 'in_progress' | 'completed' | 'cancelled';
  date: string;
  address: string;
  totalAmount: number;
}
""")

write_file('data/mock.ts', """
import { ServiceCategory, Service, Technician, Booking } from '../types';

export const categories: ServiceCategory[] = [
  { id: '1', name: 'Electrician', icon: 'flash' },
  { id: '2', name: 'Plumber', icon: 'water' },
  { id: '3', name: 'AC Repair', icon: 'snow' },
  { id: '4', name: 'Cleaning', icon: 'color-wand' },
  { id: '5', name: 'Carpenter', icon: 'hammer' },
  { id: '6', name: 'Pest Control', icon: 'bug' },
  { id: '7', name: 'Painting', icon: 'brush' },
  { id: '8', name: 'More', icon: 'grid' },
];

export const services: Service[] = [
  {
    id: 's1',
    categoryId: '1',
    name: 'Circuit Breaker Replacement',
    description: 'Replace faulty circuit breakers and restore power safely.',
    price: 85,
    estimatedTime: '45-60 mins',
    isEmergency: true,
  },
  {
    id: 's2',
    categoryId: '2',
    name: 'Emergency Plumbing',
    description: 'Fix burst pipes, severe leaks, or overflowing toilets immediately.',
    price: 95,
    estimatedTime: '1 hr',
    isEmergency: true,
  },
  {
    id: 's3',
    categoryId: '3',
    name: 'AC Gas Refill',
    description: 'Top up AC refrigerant for optimal cooling.',
    price: 60,
    estimatedTime: '45 mins',
  },
];

export const technicians: Technician[] = [
  {
    id: 't1',
    name: 'Marcus Chen',
    rating: 4.9,
    jobsCompleted: 124,
    distance: '2.4 km',
    eta: '12 mins',
    pricePerHour: 85,
    avatar: 'https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80',
    isVerified: true,
    type: 'Expert Plumber',
  },
  {
    id: 't2',
    name: 'Marcus Rivera',
    rating: 4.9,
    jobsCompleted: 1200,
    distance: '1.2 km',
    eta: '12 mins',
    pricePerHour: 90,
    avatar: 'https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80',
    isVerified: true,
    type: 'Master Electrician',
  },
];

export const user = {
  name: 'Sri',
  location: 'Indiranagar, Bangalore',
  avatar: 'https://images.unsplash.com/photo-1599566150163-29194dcaad36?ixlib=rb-4.0.3&auto=format&fit=crop&w=256&q=80',
};
""")

write_file('components/Button.tsx', """
import React from 'react';
import { TouchableOpacity, Text, StyleSheet, ActivityIndicator, ViewStyle, TextStyle } from 'react-native';
import Colors from '../constants/Colors';

interface Props {
  title: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary' | 'outline' | 'text';
  size?: 'small' | 'medium' | 'large';
  loading?: boolean;
  disabled?: boolean;
  style?: ViewStyle;
  textStyle?: TextStyle;
}

export default function Button({
  title, onPress, variant = 'primary', size = 'large', loading, disabled, style, textStyle
}: Props) {
  const getBgColor = () => {
    if (disabled) return Colors.border;
    if (variant === 'primary') return Colors.primary;
    if (variant === 'secondary') return Colors.secondary;
    if (variant === 'outline' || variant === 'text') return 'transparent';
    return Colors.primary;
  };

  const getTextColor = () => {
    if (disabled) return Colors.textSecondary;
    if (variant === 'primary' || variant === 'secondary') return Colors.white;
    if (variant === 'outline') return Colors.primary;
    if (variant === 'text') return Colors.text;
    return Colors.white;
  };

  return (
    <TouchableOpacity
      style={[
        styles.button,
        { backgroundColor: getBgColor() },
        variant === 'outline' && { borderWidth: 1, borderColor: Colors.primary },
        size === 'small' && { paddingVertical: 8, paddingHorizontal: 16 },
        size === 'medium' && { paddingVertical: 12, paddingHorizontal: 24 },
        size === 'large' && { paddingVertical: 16, paddingHorizontal: 32 },
        style
      ]}
      onPress={onPress}
      disabled={disabled || loading}
      activeOpacity={0.8}
    >
      {loading ? (
        <ActivityIndicator color={getTextColor()} />
      ) : (
        <Text style={[styles.text, { color: getTextColor() }, size === 'small' && { fontSize: 14 }, textStyle]}>
          {title}
        </Text>
      )}
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  button: {
    borderRadius: 12,
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
  }
});
""")
print("Files created")
