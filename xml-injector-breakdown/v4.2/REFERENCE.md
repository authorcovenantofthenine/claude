# XML Injector v4.2 — Modder's Quick Reference

Summary of the `XmlInjector_Modders_Documentation_v4.2` download. The bundled PDF was written for
**version 2**, so it is missing everything added in v3 and v4. This guide covers every tuning the
v4.2 script actually accepts (taken from `scripts/snippet.py`).

- Script version constant: `XML_INJECTOR_VERSION = 4` (`scripts/version.py`). The highest useful
  `xml_injector_minimum_version` is therefore **4**.
- Original author: Scumbumbo. Current maintainer: Triplis.

## Snippet header

```xml
<I c="XmlInjector" i="snippet" m="xml_injector.snippet" n="YourName_XmlInjector_Something" s="<FNV-64 of n, high bit set>">
```

| Field    | Value                                    |
|----------|------------------------------------------|
| Type     | `0x7DF2169C` (snippet)                   |
| Group    | `0x00000000`                             |
| Instance | the `s` value in hex                     |

Each top-level list below can appear **once** per snippet. To make several additions of the same kind,
put several `<U>` tuples inside the one list.

## All tunings

| Tuning | Since | What it does | Tuple contents |
|---|---|---|---|
| `xml_injector_minimum_version` | v2 | Shows a dialog after lot load if the installed injector is older | integer |
| `version_error_dialog` | v2 | Your own dialog (title/text) for the version check | optional `UiDialogOk` |
| `add_interactions_to_objects` | v1 | Adds to the objects' `_super_affordances` | `object_selection` + `_super_affordances` |
| `add_interactions_to_sims` | v1 | Shortcut for `object_sim` (14965) | list of interactions |
| `add_interactions_to_phones` | v1 | Adds to Sim `_phone_affordances` | list of interactions |
| `add_interactions_to_relationship_panel` | v1 | Adds to `_relation_panel_affordances` | list of interactions |
| `add_mixer_interactions` | v1 | Adds to any `AffordanceList` (social mixers, club lists, grounded lists…) | `mixer_snippets` + `affordances` |
| `add_buffs_to_trait` | v2 | Adds buffs to a trait's `buffs` list | `trait` + `buffs` (`buff_type`, optional `buff_reason`) |
| `add_to_loot_actions` | v2 | Appends to a `LootActions` tuning | `loot_actions_ref` + `loot_actions_to_add` |
| `add_to_random_loot_actions` | v2 | Appends weighted entries to `RandomWeightedLoot` | `random_weighted_loot_ref` + `random_loot_actions_to_add` |
| `add_states_to_objects` | v2 | Adds `states` / `state_triggers` to an **existing** state component | `object_selection` + `state_component` |
| `add_name_component_to_objects` | v2 | Adds a name component | `object_selection` + `name_component` |
| `add_object_relationships_to_objects` | v2 | Adds an object relationship component (no `icon_override`) | `object_selection` + `object_relationships_component` |
| `add_lock_aware_interactions_to_lockable_objects` | v3 | Adds to locked-computer interactions (only Sims with access see them) | `object_selection` + `super_affordances` (**no** underscore) |
| `add_satisfaction_store_rewards` | v3 | Adds reward traits and other items to the Satisfaction (Rewards) Store | `new_items`: map of `SimReward` → `award_type` + `cost` |
| `add_purchase_list_options_to_interactions` | v4 | Adds stock to `PurchasePickerInteraction`s | `interactions_to_add_to` + `purchase_list_options` (`all_items`, `specific_items`, `inventory_items`, `random_items`, `tested_items`) |
| `add_picker_dialog_categories_to_interactions` | v4 | Adds filter tabs to purchase pickers | `interactions_to_add_to` + `picker_dialog_categories` (`tag`, `icon`, `tooltip`) |

## Object selection variants

Used by every `*_to_objects` tuning.

| Variant (`t=`) | Field | Notes |
|---|---|---|
| `object_list` | `object_list` (list of GameObject IDs) | Most precise |
| `objects_matching_name` | `partial_name` | Substring match; `object_trash` also matches `object_trashcan` |
| `objects_with_affordance` | `affordance` | Best for families like sofas or computers; picks up EP and CC objects |
| `objects_with_tag` | `tag` (`<E>`) | Depends on CC creators tagging objects correctly |

Useful selector: `225064` (`computer_Locking_LockForEveryone`) selects all lockable computers.

## Ready-made examples

| File | Shows |
|---|---|
| `examples/*AddLockAwareInteractionsToLockableObjectsTest.xml` | Lock-aware computer interaction |
| `examples/*AddSatisfactionStoreRewards.xml` | Two reward traits at 150 and 100 points |
| `examples/*AddPurchaseListOptionsToInteractions.xml` | Adds the `Func_Purchase_Vacation_Furniture` tag to the computer book-buying picker |
| `examples/*AddPickerDialogCategoriesToInteractions.xml` | Adds a "Furniture" category tab to the same picker |
| `test_package_xml/*AddInteractionTest_Modders.SnippetTuning.xml` | One snippet that uses objects, sims, phones, the relationship panel and mixers |

The PDF has a v2 example of every other tuning. Its text is in `Modders_Documentation_v2_pdf_text.txt`.

## Detecting a missing injector

Include the drama node `Scumbumbo_dialogDramaNode_XmlInjector_Detection` from
`XmlInjector_Detector.package`, plus its string table, in your mod. **Do not change its instance ID**
`15419684579670968912` (`0xD5FDB96D9FDB4A50`). Change only the text. `scripts/detection.py` turns the
drama node off when the injector loads. If the injector is missing, the dialog appears around 3–4 AM
Sim time, every 48 Sim hours.

## Problems in the original docs

1. **Broken XML in the PDF's name-component example:** `<E n="tag">Func_Fridge</T>` must end in `</E>`.
   Copied as-is, it will not parse.
2. **Wrong name in the PDF:** the feature summary says `add_buffs_to_traits`, but the code and the
   section heading use `add_buffs_to_trait` (singular). The plural is ignored.
3. **Two PDF examples share an ID:** Test4 and Test6 both use `s="10608251930441092053"`. Give every
   snippet its own hash.
4. **`add_lock_aware_interactions_to_lockable_objects` uses `super_affordances`** (no leading
   underscore). Every other object tuning uses `_super_affordances`.
5. The README is titled "v4" while the download is v4.2. The script reports version 4.
6. `debug.log` in the zip holds only two stray Windows Chromium errors and can be ignored.

## Troubleshooting checklist

1. Put `XmlInjector_Script_Test_Modders_v4.2.package` in Mods. The test interaction should appear on
   mailboxes, computers, Sims, the phone, the relationship panel and friendly chats.
2. Use the Sims Log Enabler with `ENABLE_LOGGING_AT_STARTUP = True` and read `XmlInjector.log`.
   Exceptions in snippets go there, not to `LastExceptions.txt`.
3. Search `Tuning.log` for your snippet's **decimal** instance ID to find tuning errors.
4. A loot `actions` entry that could loop back on itself is rejected, and the error is written to the log.
5. Tell players to install XML Injector themselves. Don't bundle the script with your mod.
