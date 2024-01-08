import type { Metadata } from 'next'
import { Inter, Montserrat } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })
const montsterrat = Montserrat({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'NeurJAM',
  description: 'One Stop Solution for LLMs',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={montsterrat.className}>{children}</body>
    </html>
  )
}
