import {useForm} from "react-hook-form";
import {zodResolver} from "@hookform/resolvers/zod";
import {type LoginSchema, loginSchema} from "../../schemas/forms/LoginSchema.ts";
import {useState} from "react";
import {useLoginStore} from "./loginSlice.ts";

function LoginForm() {
    // @ts-ignore
    const {register, handleSubmit, formState: {errors}} = useForm<LoginSchema>({
        resolver: zodResolver(loginSchema)
    });

    // @ts-ignore
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const login = useLoginStore(state => state.logar);

    const onSubmit = (data: LoginSchema) => {
        try {
            setLoading(true);
            login(data);
        } catch (e) {
            console.log(e);
            setError("Falha no login");
        } finally {
            setLoading(false);
        }
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)} className="max-w-sm mx-auto p-4 space-y-4">
            <h2 className="text-xl font-semibold">Login</h2>
            <div>
                <input
                    type="email"
                    placeholder="Email"
                    {...register("email")}
                    className="w-full border rounded p-2"
                />
                {errors.email && <p className="text-red-500 text-sm">{errors.email.message}</p>}
            </div>
            <div>
                <input
                    type="password"
                    placeholder="Senha"
                    {...register("password")}
                    className="w-full border rounded p-2"
                />
                {errors.password && <p className="text-red-500 text-sm">{errors.password.message}</p>}
            </div>

            {error && <p className="text-red-500 text-sm">{error}</p>}

            <button type="submit" disabled={loading}
                    className="bg-indigo-600 text-white w-full py-2 rounded">
                {loading ? 'Entrando...' : 'Entrar'}
            </button>
        </form>
    );
}

export default LoginForm;