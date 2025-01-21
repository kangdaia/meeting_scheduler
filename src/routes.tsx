import {
    type RouteConfig,
    layout,
    route,
} from "@react-router/dev/routes";

export default [
    layout("./app/layout.tsx", [
        route("*?", "catchall.tsx"),
    ])
//   {
//     path: "/",
//     file: "./routes/layout.tsx",
//     children: [
//       {
//         index: true,
//         file: "./routes/home.tsx",
//       },
//       {
//         path: "home",
//         file: "./routes/home.tsx",
//       },
//       {
//         path: "todos",
//         file: "./routes/todos.tsx",
//         children: [
//           {
//             path: ":id",
//             file: "./routes/todo.tsx",
//           },
//         ],
//       },
//     ],
//   },
] satisfies RouteConfig;
