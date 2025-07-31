import {Navigate, Outlet} from "react-router-dom";
import {useLoginStore} from "../features/login/loginSlice.ts";

export function AuthGuard() {
    const user = useLoginStore(state => state.login)
    if (!user) {
        return <Navigate to="/login" replace />
    }

    return <Outlet />
}