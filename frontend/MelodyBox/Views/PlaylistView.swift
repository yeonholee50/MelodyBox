import SwiftUI

struct PlaylistView: View {
    @State private var playlistName: String = ""
    @EnvironmentObject var userSession: UserSession
    
    var body: some View {
        VStack {
            TextField("Playlist Name", text: $playlistName)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            Button(action: {
                createPlaylist()
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
    
    private func createPlaylist() {
        // Perform playlist creation action
        userSession.apiService.createPlaylist(name: playlistName) { result in
            switch result {
            case .success(let playlist):
                print("Playlist created successfully: \(playlist)")
            case .failure(let error):
                print("Failed to create playlist: \(error)")
            }
        }
    }
}

