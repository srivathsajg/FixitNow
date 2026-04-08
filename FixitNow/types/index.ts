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
