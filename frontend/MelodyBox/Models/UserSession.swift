import Foundation

class UserSession: ObservableObject {
    // Properties
    @Published var isLoggedIn: Bool = false
    
    // Dependencies
    let apiService: ApiService
    
    init(apiService: ApiService) {
        self.apiService = apiService
    }
    
    func login(email: String, password: String, completion: @escaping (Result<User, Error>) -> Void) {
        apiService.login(email: email, password: password) { result in
            switch result {
            case .success(let user):
                self.isLoggedIn = true
                completion(.success(user))
            case .failure(let error):
                completion(.failure(error))
            }
        }
    }
    
    func createPlaylist(name: String, completion: @escaping (Result<Playlist, Error>) -> Void) {
        apiService.createPlaylist(name: name) { result in
            switch result {
            case .success(let playlist):
                completion(.success(playlist))
            case .failure(let error):
                completion(.failure(error))
            }
        }
    }
    
    func logout() {
        isLoggedIn = false
        // Clear user session data, navigate to login screen, etc.
    }
}
