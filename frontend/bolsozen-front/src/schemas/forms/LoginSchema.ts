import {z} from "zod/v4";

export const loginSchema = z.object({
    email: z.string().email("Email invalido"),
    password: z.string().min(6, "Senha deve ter no minimo 6 caracteres")
});

export type LoginSchema = z.infer<typeof loginSchema>;