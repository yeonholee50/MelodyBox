import UIKit

class HomeViewController: UIViewController {

    let titleLabel: UILabel = {
        let label = UILabel()
        label.text = "Welcome to MelodyBox!"
        label.textAlignment = .center
        label.font = UIFont.boldSystemFont(ofSize: 20)
        return label
    }()
    
    let searchTextField: UITextField = {
        let textField = UITextField()
        textField.placeholder = "Search for a song"
        textField.borderStyle = .roundedRect
        return textField
    }()
    
    let searchButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Search", for: .normal)
        button.addTarget(self, action: #selector(searchButtonTapped), for: .touchUpInside)
        return button
    }()
    
    // MARK: - Lifecycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    // MARK: - UI Setup
    
    private func setupUI() {
        view.backgroundColor = .white
        
        view.addSubview(titleLabel)
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        titleLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        titleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 40).isActive = true
        
        view.addSubview(searchTextField)
        searchTextField.translatesAutoresizingMaskIntoConstraints = false
        searchTextField.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        searchTextField.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
        searchTextField.widthAnchor.constraint(equalToConstant: 200).isActive = true
        
        view.addSubview(searchButton)
        searchButton.translatesAutoresizingMaskIntoConstraints = false
        searchButton.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        searchButton.topAnchor.constraint(equalTo: searchTextField.bottomAnchor, constant: 20).isActive = true
    }
    
    // MARK: - Actions
    
    @objc private func searchButtonTapped() {
        guard let query = searchTextField.text, !query.isEmpty else {
            showAlert(message: "Please enter a search query")
            return
        }
        
        // Perform search logic here
        print("Search button tapped with query: \(query)")
    }
    
    private func showAlert(message: String) {
        let alert = UIAlertController(title: nil, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alert, animated: true, completion: nil)
    }
}
