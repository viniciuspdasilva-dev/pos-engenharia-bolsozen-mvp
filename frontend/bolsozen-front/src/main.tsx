import {StrictMode} from 'react'
import {createRoot} from 'react-dom/client'
import './index.css'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import LoginForm from "./features/login/LoginForm.tsx";
import {AuthGuard} from "./guard/AuthGuard.tsx";
import App from "./App.tsx";

createRoot(document.getElementById('root')!).render(
  <StrictMode>
      <BrowserRouter>
          <Routes>
              <Route  path="/login" element={<LoginForm />}/>

              <Route element={<AuthGuard />}>
                  <Route path="/" element={<App />} />
              </Route>
          </Routes>
      </BrowserRouter>
  </StrictMode>,
)
