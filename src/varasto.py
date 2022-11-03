class Varasto:
    def __init__(self, tilavuus: float = 0, alku_saldo: float =0) -> None:
        """
        Args:
            tilavuus (float): Total allowed space in the warehouse
            alku_saldo (float, optional): starting saldo. Defaults to 0.
        """
        self.tilavuus = max(tilavuus, 0.0)
        self.saldo = max(alku_saldo, 0.0)
        self.saldo = min(self.saldo, self.tilavuus)

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self) -> float:
        """Check how much there is space left in the warehouse

        Returns:
            float: available space in warehouse
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara: float) -> None:
        """Add item to the warehouse

        Args:
            maara (float: item to add to the warehouse
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara: float) -> float:
        """Take item from the warehouse

        Args:
            maara (float): item to take from the warehouse

        Returns:
            float: if maara is more than the saldo, return all you could
            else return the maara.
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
