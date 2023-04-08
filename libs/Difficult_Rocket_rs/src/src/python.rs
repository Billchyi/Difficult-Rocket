/*
 * -------------------------------
 * Difficult Rocket
 * Copyright © 2020-2023 by shenjackyuanjie 3695888@qq.com
 * All rights reserved
 * -------------------------------
 */

pub mod data {
    use std::collections::HashMap;

    use pyo3::prelude::*;

    use crate::sr1_data::part_list::RawPartList;
    use crate::sr1_data::ship::RawShip;
    use crate::types::sr1::{SR1PartList, SR1PartType, SR1Ship};
    use crate::types::sr1::{SR1PartListTrait, SR1ShipTrait};

    #[pyclass]
    #[pyo3(name = "SR1PartType_rs")]
    pub struct PySR1PartType {
        pub data: SR1PartType,
    }

    #[pymethods]
    impl PySR1PartType {
        #[getter]
        fn get_name(&self) -> String { self.data.name.clone() }

        #[getter]
        fn get_mass(&self) -> f64 { self.data.mass }
    }

    impl PySR1PartType {
        pub fn new(data: SR1PartType) -> Self { Self { data } }
    }

    #[pyclass]
    #[pyo3(name = "SR1PartList_rs")]
    #[pyo3(text_signature = "(file_path = './configs/PartList.xml', list_name = 'NewPartList')")]
    pub struct PySR1PartList {
        pub part_list: SR1PartList,
    }

    #[pymethods]
    impl PySR1PartList {
        #[new]
        fn new(file_path: String, list_name: String) -> Self {
            let raw_part_list: RawPartList = RawPartList::from_file(file_path).unwrap();
            let part_list = raw_part_list.to_sr_part_list(Some(list_name));
            Self { part_list }
        }

        fn as_dict(&self) -> HashMap<String, PySR1PartType> {
            let mut dict = HashMap::new();
            for part_type in self.part_list.types.iter() {
                dict.insert(part_type.name.clone(), PySR1PartType::new(part_type.clone()));
            }
            dict
        }

        fn get_part_type(&mut self, name: String) -> Option<PySR1PartType> {
            let cache = self.part_list.get_hash_map();
            let part_type = cache.get(&name);
            if let Some(part_type) = part_type {
                Some(PySR1PartType::new(part_type.clone()))
            } else {
                None
            }
        }
    }

    #[pyclass]
    #[pyo3(name = "SR1Ship_rs")]
    #[pyo3(text_signature = "(file_path = './configs/dock1.xml', part_list = './configs/PartList.xml', ship_name = 'NewShip')")]
    pub struct PySR1Ship {
        pub ship: SR1Ship,
        pub part_list: SR1PartList,
    }

    #[pymethods]
    impl PySR1Ship {
        #[new]
        fn new(file_path: String, part_list: String, ship_name: String) -> Self {
            let raw_ship: RawShip = RawShip::from_file(file_path).unwrap();
            let ship = raw_ship.to_sr_ship(Some(ship_name));
            let part_list = SR1PartList::from_file(part_list).unwrap();
            Self { ship, part_list }
        }
    }
}

pub mod translate {
    use pyo3::prelude::*;
    use pyo3::types::PyDict;

    #[pyclass]
    pub struct TranslateConfig {
        pub raise_error: bool,
        pub replace_normal: bool,
        pub add_error: bool,
        pub is_result: bool,
        pub keep_get: bool,
        pub language: String,
    }

    #[pyclass]
    pub struct Translate {
        pub data: Py<PyDict>,
        pub get_list: Vec<(String, bool)>,
        pub config: TranslateConfig,
    }
}
