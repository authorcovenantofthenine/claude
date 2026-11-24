# Your first mod: Mod Constructor v5 + XML Injector

**Goal:** a new interaction you can click on a Sim that gives a moodlet (a buff). An example is
"Say a Little Prayer", which gives a happy moodlet. Once this works, the same steps carry over to
bigger ideas.

## Which tool does what

| Piece | Made by | Why |
|---|---|---|
| The interaction (name, animation, moodlet, tests) | **Mod Constructor v5** | It writes this XML for you |
| Attaching the interaction to Sims | **XML Injector snippet** (`XmlInjector_Snippet_TEMPLATE.xml`) | Avoids overriding EA's `object_sim`, which conflicts with almost every other interaction mod |

> **Check first:** Mod Constructor may already be able to attach interactions to Sims for you. In
> the past, Zerbu's tools have done this, sometimes through XML Injector itself. If your interaction
> element has a setting like "add to Sims" or "XML Injector", use that and **skip Part 2**. Doing both
> adds the interaction twice. I couldn't confirm the exact v5 menus, so follow what your copy shows.

## Part 1 — Make the interaction in Mod Constructor v5

1. Start a new project. Set your **creator name**. It goes at the front of every tuning name, so
   pick something unique, such as `Chloe` or your modding handle.
2. Add an **Interaction** element (for a social one, pick the social/mixer interaction type if v5
   offers one). Choose:
   - **Display name**, e.g. "Say a Little Prayer"
   - **Target:** self (click your own Sim) or another Sim
   - **Animation:** pick a simple existing one to start
   - **Outcome:** give a buff. Either pick an existing EA buff or add a **Buff** element for your own
     moodlet.
3. Export or build the `.package`.
4. Note the interaction's **instance ID** (decimal). You can find it in Mod Constructor's element
   details, or by opening the exported package in Sims 4 Studio and looking at the
   `InteractionTuning` resource's `s="..."` value.

## Part 2 — Add the XML Injector snippet

1. Open `XmlInjector_Snippet_TEMPLATE.xml`. Replace every `INTERACTION_ID_FROM_MOD_CONSTRUCTOR` with
   the number from step 4 above.
2. Optional: rename the snippet to use your creator name, e.g. `Chloe_FirstMod_XmlInjectorSnippet`,
   then get its new IDs:

   ```bash
   python hash_name.py "Chloe_FirstMod_XmlInjectorSnippet"
   ```

   Put the printed `s="..."` into the `<I ...>` line and use the printed **Instance** hex in step 3.
3. Add the snippet to your package:
   - If Mod Constructor v5 lets you add a **custom XML / snippet** element, paste it there.
   - Otherwise, open the exported `.package` in **Sims 4 Studio**. Choose *Tools → Create → Add* (or
     *Add* in the Warehouse tab). Use Type `0x7DF2169C` (Snippet), Group `0x00000000`, and the
     Instance from the comment at the top of the template. Paste the XML in, then save.

## Part 3 — Test

1. Put **XML Injector** itself (the `.ts4script` from the official download, not this docs zip) and
   your `.package` in `Documents/Electronic Arts/The Sims 4/Mods`. Script mods must be at most **one
   folder deep**.
2. In the game options, turn on **Enable Custom Content and Mods** and **Script Mods Allowed**, then
   restart the game.
3. Optional sanity check: add `XmlInjector_Script_Test_Modders_v4.2.package` from the docs zip.
   Mailboxes should then have an "XML Injector Test" interaction. Remove it afterwards.
4. Load a household and click a Sim (or your own Sim for a self interaction). Your interaction should
   be there.

## If it doesn't show up

| Symptom | Likely cause |
|---|---|
| Mailbox test interaction is missing too | XML Injector isn't installed or script mods are off |
| Test works, yours doesn't | Wrong interaction ID in the snippet, or the snippet's Type/Group/Instance are wrong |
| Shows on the wrong Sim (or not on self) | Interaction target settings in Mod Constructor |
| Shows twice | Mod Constructor already attached it, so remove your snippet (see "Check first") |
| Still stuck | Install the Sims Log Enabler and read `XmlInjector.log`, then search `Tuning.log` for your snippet's decimal ID |

## Before you publish

- Tell users to **download XML Injector separately**, and link the official page. Don't bundle it.
- Optional: add the detector drama node from `XmlInjector_Detector.package` so players get a warning
  if XML Injector is missing. Never change its instance ID. See
  `../xml-injector-breakdown/v4.2/REFERENCE.md`.

## Next ideas using the same injector

- Add the interaction to the **phone** (`add_interactions_to_phones`) or to **computers**
  (`add_interactions_to_objects` with selector affordance `225064`).
- Make it a **chat topic** (`add_mixer_interactions` → `24508` friendly non-touching mixers).
- Sell a custom trait in the **Rewards Store** (`add_satisfaction_store_rewards`).
