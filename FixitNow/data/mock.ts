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
