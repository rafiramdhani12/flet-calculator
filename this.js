class Hewan {
  constructor(nama) {
    this.nama = nama;
  }

  berbicara() {
    console.log(`hewan ${this.nama} berbicara`);
  }
}

const kucing = new Hewan("kucing");
kucing.berbicara();

// class Chelsea {
//   constructor() {
//     let count = 0;
//     while (count < 4) {
//       count++;
//       console.log("🧑🏿".repeat(count));
//     }
//   }
// }

// // Membuat instance dari kelas Chelsea
// const myChelsea = new Chelsea();

const chelsea = () => {
  let count = 0;
  while (count < 4) {
    count++;
    console.log("🧑🏿".repeat(count));
  }
};

chelsea();
