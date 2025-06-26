import React, { useState } from 'react'
import { CountdownCircleTimer } from 'react-countdown-circle-timer'

export default function Timer() {
  const [playing, setPlaying] = useState(false)

  const handleStart = () => {
    setPlaying(true)
  }

  const handleStop = () => {
    setPlaying(false)
  }

  return (
    <>
      <CountdownCircleTimer
        isPlaying={playing}
        duration={15 * 60}
        colors={['#004777', '#F7B801', '#A30000', '#A30000']}
        colorsTime={[7, 5, 2, 0]}
      >
        {(renderProps) => <FormatDisplay {...renderProps} />}
      </CountdownCircleTimer>
      <div>
        <button onClick={handleStart}>Start</button>
        <button onClick={handleStop}>Stop</button>
      </div>
    </>
  )
}

const FormatDisplay = ({ remainingTime }: { remainingTime: number }) => {
  const minutes = Math.floor(remainingTime / 60)
  const seconds = remainingTime % 60
  return (
    <p>
      {minutes}:{seconds.toString().padStart(2, '0')}
    </p>
  )
}
