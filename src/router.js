import { createBrowserRouter } from "react-router-dom";
import React, { lazy } from "react";
//import Homepage from './components/Homepage/Homepage'; // Assurez-vous que le chemin est correct
//import PlayOnline from './components/PlayOnline/PlayOnline'; // Assurez-vous que le chemin est correct
//import PlayComputer from './components/PlayComputer/PlayComputer'; // Assurez-vous que le chemin est correct

const App = lazy(() => import("./App"));
const Homepage = lazy(() => import("./components/Homepage/Homepage"));
const About = lazy(() => import("./components/Header/components/About/About"));
const UserGuide = lazy(() =>
  import("./components/Header/components/UserGuide/UserGuide")
);
const ContactUs = lazy(() =>
  import("./components/Header/components/ContactUs/ContactUs")
);
const PlayOnline = lazy(() => import("./components/PlayOnline/PlayOnline"));
const PlayLocal = lazy(() => import("./components/PlayLocal/PlayLocal"));
const PlayComputer = lazy(() =>
  import("./components/PlayComputer/PlayComputer")
);
const PlayEasy = lazy(() =>
  import("./components/PlayComputer/PlayEasy/PlayEasy")
);
const PlayMedium = lazy(() =>
  import("./components/PlayComputer/PlayMedium/PlayMedium")
);
const PlayDifficult = lazy(() =>
  import("./components/PlayComputer/PlayDifficult/PlayDifficult")
);
const CreateParty = lazy(() =>
  import("./components/PlayOnline/CreateParty/CreateParty")
);
const JoinParty = lazy(() =>
  import("./components/PlayOnline/JoinParty/JoinParty")
);
const GameRoom = lazy(() => import("./components/PlayOnline/GameRoom"));
export const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <Homepage />,
      },
      {
        path: "/about",
        element: <About />,
      },
      {
        path: "/contact-us",
        element: <ContactUs />,
      },
      {
        path: "/user-guide",
        element: <UserGuide />,
      },
      {
        path: "/play-online",
        element: <PlayOnline />,
      },
      {
        path: "/play-local",
        element: <PlayLocal />,
      },
      {
        path: "/play-computer",
        element: <PlayComputer />,
      },
      {
        path: "/play-computer/play-easy",
        element: <PlayEasy />,
      },
      {
        path: "/play-computer/play-medium",
        element: <PlayMedium />,
      },
      {
        path: "/play-computer/play-difficult",
        element: <PlayDifficult />,
      },
      {
        path: "/play-online/create-party",
        element: <CreateParty />,
      },
      {
        path: "/play-online/join-party",
        element: <JoinParty />,
      },
      {
        path: "/game-room/:gameNumber", // Route avec un paramètre d'URL pour le numéro de partie
        element: <GameRoom />,
      },
    ],
  },
]);
