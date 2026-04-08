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
