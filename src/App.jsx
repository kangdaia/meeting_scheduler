import { useState } from 'react'
import './App.css'
import { Theme } from "@radix-ui/themes";
import { ThemeProvider } from "next-themes";

function App() {

  return (
    <ThemeProvider attribute="class">
      <Theme accentColor="ruby" grayColor="mauve" panelBackground="translucent">
        <div className="font-bold">
          가나다라마바사 아자차카타파하
        </div>
        <p className="read-the-docs">
          Click on the Vite and React logos to learn more
        </p>
      </Theme>
    </ThemeProvider>
  )
}

export default App
