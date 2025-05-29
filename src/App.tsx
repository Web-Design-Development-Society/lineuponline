import { useEffect, useState } from 'react'
import Timer from './components/Timer'
import Header from './components/Header'

type Period = 'Focus' | 'Long Break' | 'Short Break'

function App() {
  const [cyclesCompleted, setCyclesCompleted] = useState<number>(0)
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [currentPeriod, setCurrentPeriod] = useState<Period>('Focus')

  useEffect(() => {
    setCyclesCompleted(1)
  }, [])

  return (
    <>
      <Header />
      <h1>Pomodoro</h1>
      <p>Cycles Completed: {cyclesCompleted}</p>
      <Timer></Timer>
    </>
  )
}

export default App
