import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Effects from './Effects.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Effects></Effects>
  </StrictMode>,
)