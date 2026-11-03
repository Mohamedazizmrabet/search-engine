import { Link, Route, Routes } from 'react-router'
import HomePage from './pages/HomePage'
import SearchPage from './pages/SearchPage'
import AdminPage from './pages/AdminPage'

function App() {
  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <header className="bg-white shadow">
        <nav className="mx-auto flex max-w-6xl gap-6 px-4 py-3">
          <Link to="/" className="font-bold">
            Course Search
          </Link>
          <Link to="/admin" className="ml-auto text-gray-600">
            Admin
          </Link>
        </nav>
      </header>

      <main className="mx-auto max-w-6xl px-4 py-8">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/admin" element={<AdminPage />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
