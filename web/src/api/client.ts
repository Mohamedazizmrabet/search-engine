// Every call to the NestJS API goes through this file.
const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:3000'

export async function apiGet<T>(path: string): Promise<T> {
  const response = await fetch(`${API_URL}${path}`)
  if (!response.ok) {
    throw new Error(`API error ${response.status}`)
  }
  return (await response.json()) as T
}
