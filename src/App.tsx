import React, { Suspense } from 'react'
import { Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Nav from './components/Nav'

const Pomodoro = React.lazy(() => import('./components/Pomodoro'))

function App() {
  return (
    <>
      <Header />
      <Nav />
      <Suspense fallback={<p>LOADING</p>}>
        <Routes>
          <Route path="/" element={<p>HOMIE</p>} /> {/* Home Page */}
          <Route path="/pomodoro" element={<Pomodoro />} />
        </Routes>
      </Suspense>
      {/* TODO: Add footer */}
    </>
  )
}

export default App
