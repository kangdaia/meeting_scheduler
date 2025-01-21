import { useLoaderData } from "react-router";

export async function clientLoader() {
    return {
        title: "About",
    };
}

export default function About() {
    const data = useLoaderData();
    return (
        <div>{data.title}</div>
    );
}

// clientAction, ErrorBoundary, etc.