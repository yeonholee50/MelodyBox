import SwiftUI

struct ProfileView: View {
    var username: String
    var email: String
    
    var body: some View {
        VStack {
            Text("User Profile")
                .font(.title)
                .padding()
            
            // Display profile information
            Text("Username: \(username)")
                .padding()
            Text("Email: \(email)")
                .padding()
            
            
            Button(action: {
                logout()
            }) {
                Text("Logout")
                    .padding()
                    .background(Color.red)
                    .foregroundColor(.white)
                    .cornerRadius(5)
            }
            .padding()
        }
    }
    
    private func logout() {
        // Perform logout action
        print("Logging out")
        // Add logic to perform logout (like clear user session)
    }
}
