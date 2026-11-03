import { useEffect, useState } from 'react'
import { apiGet } from '../api/client'

interface Hello {
  message: string
  database: string
  search: string
}

// TODO: search bar at the top + course cards grouped by subject (see docs/api-contract.md)
function HomePage() {
  const [hello, setHello] = useState<Hello | null>(null)
  const [error, setError] = useState('')

  useEffect(() => {
    apiGet<Hello>('/')
      .then(setHello)
      .catch(() => setError('The API is not reachable'))
  }, [])

  return (
    <div className="space-y-6">
      <input
        type="search"
        placeholder="Search a concept in your courses (e.g. API, TF-IDF, Docker)"
        className="w-full rounded-lg border border-gray-300 px-4 py-3 text-lg"
      />

      <div className="rounded-lg bg-white p-4 shadow">
        <h2 className="mb-2 font-semibold">Connection check</h2>
        {error && <p className="text-red-600">{error}</p>}
        {hello && (
          <ul className="text-sm">
            <li>API: {hello.message}</li>
            <li>Database: {hello.database}</li>
            <li>Search service: {hello.search}</li>
          </ul>
        )}
      </div>
    </div>
  )
}

export default HomePage
