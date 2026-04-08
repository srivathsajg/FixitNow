import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

def basic_screen(title):
    return f"""
import React from 'react';
import {{ View, Text, StyleSheet }} from 'react-native';
import Colors from '../../constants/Colors';

export default function {title.replace(' ', '')}Screen() {{
  return (
    <View style={{styles.container}}>
      <Text style={{styles.title}}>{title}</Text>
    </View>
  );
}}

const styles = StyleSheet.create({{
  container: {{ flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: Colors.background }},
  title: {{ fontSize: 24, fontWeight: '700', color: Colors.text }}
}});
"""

write_file('app/service/[id].tsx', basic_screen('Service Category'))
write_file('app/service/detail.tsx', basic_screen('Service Detail'))
write_file('app/booking/select-technician.tsx', basic_screen('Select Technician'))
write_file('app/booking/payment.tsx', basic_screen('Payment'))
write_file('app/booking/completed.tsx', basic_screen('Completed'))
write_file('app/booking/review.tsx', basic_screen('Review'))
write_file('app/profile/addresses.tsx', basic_screen('Addresses'))
write_file('app/notifications.tsx', basic_screen('Notifications'))

