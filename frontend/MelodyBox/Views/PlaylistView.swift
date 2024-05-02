import SwiftUI

struct PlaylistView: View {
    @State private var playlistName: String = ""
    
    var body: some View {
        VStack {
            TextField("Playlist Name", text: $playlistName)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            Button(action: {
                // Perform playlist creation action
            }) {
                Text("Create Playlist")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(5)
            }
        }
        .padding()
    }
}
