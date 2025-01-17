import { useState } from 'react'
import Layout from '@/app/layout'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="flex flex-row w-full h-full">
      <Layout>
        {/* 여기에 메인 콘텐츠를 넣으세요 */}
        <div className="p-4">
          <h1>메인 페이지</h1>
          <p>여기에 콘텐츠가 들어갑니다.</p>
        </div>
      </Layout>
    </div>
  )
}

export default App
