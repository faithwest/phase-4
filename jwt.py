# // Import the jsonwebtoken library
# const jwt = require('jsonwebtoken');

# // Secret key for signing the token (keep this safe)
# const secretKey = 'your-secret-key';

# // User payload to include in the token (usually user data)
# const userPayload = {
#     id: 1,
#     username: 'faithngeno',
#     role: 'user'
# };

# // Generate JWT token
# function generateToken(user) {
#     return jwt.sign(user, secretKey, { expiresIn: '1h' }); // Token expires in 1 hour
# }

# // Verify JWT token
# function verifyToken(token) {
#     try {
#         const decoded = jwt.verify(token, secretKey);
#         return decoded;
#     } catch (err) {
#         return 'Invalid or expired token';
#     }
# }

# // Generate a new token
# const token = generateToken(userPayload);
# console.log('Generated JWT Token:', token);

# // Verifying the token
# const decodedPayload = verifyToken(token);
# console.log('Decoded Payload:', decodedPayload);

# // Example of an invalid token (use this to test error handling)
# const invalidToken = 'invalid-token-example';
# console.log('Invalid Token Test:', verifyToken(invalidToken));
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]

Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
