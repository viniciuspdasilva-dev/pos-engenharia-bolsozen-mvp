import {create} from "zustand/react";

interface Login {
    email: string;
    password: string;
}

interface LoginSlice {
    login: Login | null;
    logar: (login: Login) => void;
    logout: () => void;
}

export const useLoginStore = create<LoginSlice>((set) => ({
    login: null,
    logar: (login) => set({login}),
    logout: () => set({login: null})
}))