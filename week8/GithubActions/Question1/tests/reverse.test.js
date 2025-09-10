const { reverseString } = require('../src/reverse');

test('reverses "hello" to "olleh"', () => {
  expect(reverseString('hello')).toBe('olleh');
});

test('reverses an empty string to ""', () => {
  expect(reverseString('')).toBe('');
});

test('reverses "JavaScript" to "tpircSavaJ"', () => {
  expect(reverseString('JavaScript')).toBe('tpircSavaJ');
});